import pandas as pd 
import numpy as np 

data = pd.read_csv("C:/xampp/htdocs/houseviz/heat/dummy.csv")

ar = data.values.tolist()

print(ar)