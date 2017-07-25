import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

print("Welcome to House.Viz")
print("Please select your budget range :")
print("1. $50000-$100000")
print("2. $100000-$200000")
print("3. $200000-$300000")
print("4. $300000-$400000")
print("5. $400000-$500000")
print("6. $500000-$600000")
print("7. $600000-$700000")
print("8. $700000-$800000")
print("9. $800000-$900000")
print("10. $900000-$1000000")
print("11. $1000000-$1500000")
print("12. $1500000-$5000000")
print("13. $5000000-$7750000")

price = input()
price=int(price)
#pritn("price="+str())
print("Please select your desized house area:")
print("1. 300 - 1000 sq.ft")
print("2. 1000 - 1500 sq.ft")
print("3. 1500 - 2000 sq.ft")
print("4. 2000 - 2500 sq.ft")
print("5. 2500 - 3000 sq.ft")
print("6. 3000 - 4000 sq.ft")
print("7. 4000 - 5000 sq.ft")
print("8. 5000 - 6000 sq.ft")
print("9. 6000 - 7000 sq.ft")
print("10. 7000+ sq.ft")

area = input()
area=int(area)
print("How much are you willing to walk ?")
print("1.500 meters")
print("2.1000 meters")
distance = input()
ditance = int(distance)
if price == 1:
    print("yes")
    minp=50000
    maxp=100000
elif price==2:
    minp=100000    
    maxp=200000
elif price==3:
    minp=200000    
    maxp=300000
elif price==4:
    minp=300000    
    maxp=400000    
elif price==5:
    minp=400000    
    maxp=500000    
elif price==6:
    minp=500000    
    maxp=600000
elif price==7:
    minp=600000    
    maxp=700000
elif price==8:
    minp=700000    
    maxp=800000
elif price==9:
    minp=800000    
    maxp=900000
elif price==10:
    minp=900000    
    maxp=1000000
elif price==11:
    minp=1000000    
    maxp=1500000
elif price==12:
    minp=1500000    
    maxp=5000000 
elif price==13:
    minp=5000000    
    maxp=7750000   
    
    
if area==1:
    mina=300
    maxa=1000
elif area==2:
    mina=1000    
    maxa=1500
elif area==3:
    mina=1500    
    maxa=2000
elif area==4:
    mina=2000    
    maxa=2500    
elif area==5:
    mina=2500    
    maxa=3000    
elif area==6:
    mina=3000    
    maxa=4000
elif area==7:
    mina=4000    
    maxa=5000
elif area==8:
    mina=5000    
    maxa=6000
elif area==9:
    mina=6000    
    maxa=7000
elif area==10:
    mina=7000    
    maxa=15000
       
dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset.csv")

count=0
for index,row in dataset.iterrows():    
    area=row["LAND.SQUARE.FEET"]
    price=row["SALE.PRICE"]
    if price>minp and price<maxp:
        if area>mina and area<maxa:
            count+=1 

print("Yay! We've found "+str(count)+" houses that fit your needs")      
    