import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

dataset = pd.read_csv("C:/Users/admin/Desktop/Stevens Internship 2017/Datasets/Final/final_plotset.csv")
#dataset = pd.read_csv("C:/Users/admin/Desktop/nyc_clean62.csv")
dataset["SALE.PRICE"].describe()
#-----------------------Normalization------------------------------------------

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
dataset = scaler.fit_transform(dataset)

area = np.array(dataset[:100,1:2])
price = np.array(dataset[:100,2:3])

#------------------------Visualization-----------------------------------------
#plt.plot(price,area)
#plt.xticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000])
#set(gca,'XTick',[0:500:10000]);
#plt.xlabel("Area of houses(sq.feet)")
#plt.ylabel("Price of house(USD $)")
#plt.show()

plt.hist(price,bins=5)
plt.show()
