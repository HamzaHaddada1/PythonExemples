from urllib.request import urlopen
import json
import xlrd
from xlwt import Workbook
import csv
import time


wb=Workbook()



file_location="C:/Users/Hamza/Downloads/German_cities.xls"
work=xlrd.open_workbook(file_location)
sheet= work.sheet_by_index(0)
i=1

sheet1=wb.add_sheet('sheet 1')
sheet1.write(0,0,'ZIP')
sheet1.write(0,1,'Lat')
sheet1.write(0,2,'Lng')
sleep_time=0
#key1 , key2 , key3 ,key4 are api keys
keys=['key1','key2','key3','key4']
num_key=0
while i<=10000:
	x=int(sheet.cell_value(i,0))
	print(x)
	z=str(x)
	url1= 'https://maps.googleapis.com/maps/api/geocode/json?address='
	url2=url1+z+',DE&key='
	if (i<2000):
		
		url=url2+keys[num_key]
	if(i%2000==0):
		num_key+=1


	if(i>=2000 and i<=10000):
		url=url2+keys[num_key]			
	
	if (i%100==0):
		time.sleep(5)


	json_obj=urlopen(url)
	data=json.load(json_obj)
	
	sheet1.write(i,0,z)
	for item in data['results']:
		    
			sheet1.write(i,1,str(item['geometry']['location']['lat']))
			sheet1.write(i,2,str(item['geometry']['location']['lng']))
			break
	i+=1
wb.save('zipcode.xls')
		
		
	
	
	    	
	    	  
