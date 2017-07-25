import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset.csv")

#dataset["LAND.SQUARE.FEET"].describe()
#count=0
#for index,row in dataset.iterrows():    
#    area=row["LAND.SQUARE.FEET"]
#    price=row["SALE.PRICE"]
#    if price>600000 and price<700000:
#        if area>4000 and area<5000:
#            count+=1 
#print(count)  

dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_dataset.csv")
dataset2 = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset.csv")

dataset2["City"]="0"       
dataset2["NEIGHBORHOOD"]="0"
dataset2["ADDRESS"]="0"
dataset2["ZIP.CODE"]="0"

dataset["Flag"]=0                
dataset["ID"]=0
dataset2["ID"]=0        
for index,row in dataset.iterrows():
    dataset.set_value(index,"ID",index+1)        

for index,row in dataset2.iterrows():
    dataset2.set_value(index,"ID",index+1)        
              
for index,row in dataset2.iterrows():    
    
    year = row["YEAR.BUILT"]
    area = row["LAND.SQUARE.FEET"]
    price = row["SALE.PRICE"]
    
    for i in range(len(dataset)):
        if dataset.at[i,"Flag"] == 0:
            if price == dataset.at[i,"SALE.PRICE"]:
                if area == dataset.at[i,"LAND.SQUARE.FEET"]:
                    if year == dataset.at[i,"YEAR.BUILT"]:
                    
                        city     = dataset.at[i,"City"]
                        neighbour= dataset.at[i,"NEIGHBORHOOD"]        
                        address  = dataset.at[i,"ADDRESS"]
                        zipcode  = dataset.at[i,"ZIP.CODE"]
                        full_address = address+","+neighbour+","+city
                    
                        dataset2.set_value(index,"City",city)
                        dataset2.set_value(index,"NEIGHBORHOOD",neighbour)
                        dataset2.set_value(index,"ADDRESS",full_address)
                        dataset2.set_value(index,"ZIPCODE",zipcode)
                
                        print(index,i)
                        dataset.set_value(i,"Flag",1)
                        break
                    
dataset2.to_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/full_final.csv")            