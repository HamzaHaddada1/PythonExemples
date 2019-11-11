import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soupe
import json

def jsonfile(data):
	file="sky.json"
	with open (file,"w") as fp:
		json.dump(data,fp)



url1="http://www.skysports.com/"

keys=["football/news","f1/news","cricket/news","rugby-union/news","rugby-league/news","golf/news","boxing/news","tennis/news","cycling/news","racing/news","darts/news","nfl/news","motorsport/news","netball/news","wwe/news","esports/news","olympics/news","joshua/news"]
f=0
data={}
i=0
key=0
while i<18:
	
	z=str(i)
	
	url=url1+keys[key]
	key+=1
	page1= uReq(url)
	page_html=page1.read()
	page1.close()
	page_soupe=soupe(page_html,"html.parser")
	d=1    #true
	k=1    #premiere page

	while (d!=0):  #show more condition de sortie
		z=str(k)
		container11=page_soupe.findAll("h4",{"class":"news-list__headline"})
		d=len(container11)		
		url2=url+"/more/"+z
		print(url2)
		page1= uReq(url2)
		page_html=page1.read()
		page1.close()
		page_soupe=soupe(page_html,"html.parser")
		j=0	
		k+=1       

		while j<d: #entrer dans chaque page
			
			titre=container11[j].text
			sky_url=container11[j].a["href"]	#les liens pour body
			try:		     #si page introuvable
				page2=uReq(sky_url)
				page2_html=page2.read()
				page2.close()
				page2_soupe=soupe(page2_html,"html.parser")
				container21=page2_soupe.findAll("div",{"class":"article__body article__body--lead"})
				if(len(container21)!=0):
					body=container21[0].text
					f+=j+1			
					n=str(f)
					data["titre"+n]=titre
					data["body"+n]=body	
					
			except :
				pass
			j+=1
		
		jsonfile(data)



	i+=1
	