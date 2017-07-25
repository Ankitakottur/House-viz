import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from time import sleep

print("Enter your preferred mode of travel")
print("1. Bus")
print("2. Subway")
print("3. Train")

a,b,c = map(int,input().split())

x,y,z = 9.52,5.0,5.0

x1 = x*a
y1 = y*b
z1 = z*c

trans_score = (x1+y1+z1)/6               
print("transport score :"+str(trans_score))              
sleep(1)              
a1,b1,c1 = x1/6,y1/6,z1/6
print("bus_score :"+str(a1))
sleep(0.5)
print("sub_score :"+str(b1))
sleep(0.5)
print("train_score :"+str(c1))