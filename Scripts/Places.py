 import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/set2.csv")
dataset['Schools'] = 0     
#dataset2['Bus_station'] = 0
#dataset2['Subway_station'] = 0
#dataset2['Train_station'] = 0
#dataset2['Park'] = 0
#dataset2['Police'] = 0
#dataset2['Hospital'] = 0
#dataset2['Restaurant'] = 0                
#dataset2['Grocery'] = 0
#dataset2['Bank'] = 0
#dataset2['Fire_station'] = 0
       
#------------------------------------------------------------------------------

from googleplaces import GooglePlaces,types,lang
from time import sleep

api_key = "AIzaSyBTX5Di50XFd6FsVY6tjCkhTj2sw83yqGE"
google_places = GooglePlaces(api_key)

#------------------------------------------------------------------------------
i=0
for index,row in dataset.iterrows():    
    try:
        address = row.iloc[2].strip()+","+row.iloc[1].strip()+","+row.iloc[0].strip()
        count = 0    
             
        counter=0
        query_result = google_places.nearby_search(
                location=address,radius=500,
                types=[types.TYPE_SCHOOL])
            
        if query_result.has_attributions:
            print(query_result.html_attributions)
                
        for place in query_result.places:
            counter+=1
       
        sleep(2)
    
        if query_result.has_next_page_token:
            query_result_next_page = google_places.nearby_search(
                    pagetoken=query_result.next_page_token)
               
            for place in query_result_next_page.places:
                counter+=1
            
            sleep(2)
    
            if query_result_next_page.has_next_page_token:
                query_result_next_page2 = google_places.nearby_search(
                        pagetoken=query_result_next_page.next_page_token)    
    
                for place in query_result_next_page2.places:
                    counter+=1
        print(index, counter)                
        dataset.set_value(i, 'Schools', counter)
        i=i+1
    except:
        print("Address Not Found***")
   
    
dataset.to_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/set1.csv")    
    
                     