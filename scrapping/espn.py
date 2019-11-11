import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soupe
import json

def jsonfile(data):
	file="Espn.json"
	with open (file,"w") as fp:
		json.dump(data,fp)

url="http://www.espn.com/"

page1= uReq(url)
page_html=page1.read()
page1.close()
page_soupe=soupe(page_html,"html.parser")
container11=page_soupe.findAll("h1",{"class":"contentItem__title contentItem__title--story"})
b=len(container11)
i=1
data={}
while i<b:

	z=str(i)
	title=container11[i].text
	container12=page_soupe.findAll("a",{"class":"contentItem__padding"})
	try:
		arg=container12[i]["href"]
		url2=url+arg
		page2=uReq(url2)
		page2_html=page2.read()
		page2.close()
		page2_soupe=soupe(page2_html,"html.parser")
		container21=page2_soupe.findAll("div",{"class":"article-body"})
		body=container21[0].text
		
	
	except:
		pass
	data["titre"+z]=title
	data["body"+z]=body
	jsonfile(data)
	i+=1
