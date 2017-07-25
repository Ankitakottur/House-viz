import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset500.csv")
dataset2 = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset500.csv")

#------------------------------YEAR BUILT--------------------------------------
min = 1700 
max = 2016
a = 0
b = 10
array = []
orig_array = []
df = pd.DataFrame()
df["YEAR.BUILT"] = 0
def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["YEAR.BUILT"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["YEAR.BUILT"] = array    
df["YEAR.BUILT"] = orig_array   
    
#------------------------------LAND SQUARE FEET--------------------------------------
min = 300 
max = 10300
a = 0
b = 10
array = []
orig_array = []
df["LAND.SQUARE.FEET"]=0
def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["LAND.SQUARE.FEET"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["LAND.SQUARE.FEET"] = array    
df["LAND.SQUARE.FEET"] = orig_array   

#------------------------------SALE PRICE--------------------------------------
min = 75000
max = 7750000
a = 0
b = 10
array = []
orig_array = []
df["SALE.PRICE"] = 0
def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["SALE.PRICE"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["SALE.PRICE"] = array    
df["SALE.PRICE"] = orig_array    

#------------------------------SCHOOLS--------------------------------------
min = 0 
max = 20
a = 0
b = 10
array = []
orig_array = []
df["Schools"]=0
def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Schools"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Schools"] = array    
df["Schools"] = orig_array    

dataset.to_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/dataset500.csv")
df.to_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/orig_dataset500.csv")  
  
  
#------------------------------BUS STATION--------------------------------------
min = 1 
max = 10
a = 0
b = 10
array = []
orig_array = []
df["Bus_station"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Bus_station"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Bus_station"] = array    
df["Bus_station"] = orig_array 

#------------------------------SUBWAY STATION--------------------------------------
min = 0 
max = 3
a = 0
b = 10
array = []
orig_array = []
df["Subway_station"] = 0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Subway_station"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Subway_station"] = array    
df["Subway_station"] = orig_array 

#------------------------------TRAIN STATION--------------------------------------
min = 0 
max = 2
a = 0
b = 10
array = []
orig_array = []
df["Train_station"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Train_station"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Train_station"] = array    
df["Train_station"] = orig_array 

#------------------------------HOSPITAL--------------------------------------
min = 5 
max = 25
a = 0
b = 10
array = []
orig_array = []
df["Hospitals"]=0

dataset.describe()

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset2.iterrows():
    value = float(row["Hospitals"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Hospitals"] = array    
df["Hospitals"] = orig_array 

#------------------------------POLICE STATION--------------------------------------
min = 0
max = 2
a = 0
b = 10
array = []
orig_array = []
df["Police_station"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Police_station"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Police_station"] = array    
df["Police_station"] = orig_array 

#------------------------------FIRE STATION--------------------------------------
min = 0 
max = 3
a = 0
b = 10
array = []
orig_array = []
df["Fire_station"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Fire_station"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Fire_station"] = array    
df["Fire_station"] = orig_array 

#------------------------------PARKS--------------------------------------
min = 3 
max = 20
a = 0
b = 10
array = []
orig_array = []
df["Parks"]=0
 
def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Parks"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Parks"] = array    
df["Parks"] = orig_array   
  
#------------------------------RESTAURANT--------------------------------------
min = 3
max = 56
a = 0
b = 10
array = []
orig_array = []
df["Restaurants"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Restaurants"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Restaurants"] = array    
df["Restaurants"] = orig_array   
  
#------------------------------GROCERIES--------------------------------------
min = 6 
max = 58
a = 0
b = 10
array = []
orig_array = []
df["Groceries"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Groceries"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Groceries"] = array    
df["Groceries"] = orig_array   
  
#-----------------------------MOVIE THEATRE---------------------------------------
min = 0 
max = 4
a = 0
b = 10
array = []
orig_array = []
df["Movie_Theater"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Movie_Theater"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Movie_Theater"] = array    
df["Movie_Theater"] = orig_array   
  
#-----------------------------------BANKS--------------------------------------
min = 0
max = 6
a = 0
b = 10
array = []
orig_array = []
df["Bank"]=0

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

for index,row in dataset.iterrows():
    value = float(row["Bank"])
    temp = scale(value)
    array.append(round(temp,2))
    orig_array.append(temp)    
    
dataset["Bank"] = array    
df["Bank"] = orig_array   

#--------------------------------Save------------------------------------------

dataset.to_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/dataset500.csv")
df.to_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/orig_dataset500.csv") 

  
#---------------------------HISTOGRAM------------------------------------------
#plt.hist(arr[:100])
#plt.xlabel('house')
#plt.ylabel('score')
#plt.title('House vs Score')
#plt.axis([0,10,0,10])
#plt.grid(True)
#plt.show()

 
#----------------------------------BAR PLOT------------------------------------
#y_pos = np.arange(1000)
#performance = arr[:1000] 
#plt.bar(y_pos, performance, align='center', alpha=0.5)
#plt.xticks(y_pos)
#plt.houses('Houses')
#plt.ylabel('Year Built')
#plt.title('House vs Year Built Rating') 
#plt.show()

    
#-------------------------------SCATTER PLOT-----------------------------------    
#area = np.array(dataset["LAND.SQUARE.FEET"])
#price = np.array(dataset["SALE.PRICE"])

#year = np.array(dataset["YEAR.BUILT"])
#plt.scatter(arr,year)
#plt.xlabel("Area of houses(Sq.Ft)")
#plt.ylabel("Price of house($USD)")
#plt.show()
