import pandas as pd 
import numpy as np 

df = pd.read_csv("C:/xampp/htdocs/houseviz/orig.csv")
df["date"]="0"
df["bucket"]=0
df["count"]=0
for index,row in df.iterrows():
	string = row["Head"]
	a,b,c = string.split(",")
	df.set_value(index,"date",a)
	df.set_value(index,"bucket",b)
	df.set_value(index,"count",c)

df.to_csv("C:/xampp/htdocs/houseviz/orig.csv")	