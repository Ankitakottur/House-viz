import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

min = 1950 
max = 2016
a = 0
b = 10
arr = []

def scale(x):
    return (((b-a)*(x-min))/(max-min)) + a

scale(1705)

#dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset.csv")

for index,row in dataset.iterrows():
    #value = row["YEAR.BUILT"]
    #temp = scale(value)
    temp = random.randint(1950,2000)
    arr.append(temp)     
    
plt.hist(arr,bins=10)
plt.show()    
    