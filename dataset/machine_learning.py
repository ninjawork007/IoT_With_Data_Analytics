import pandas as pd
import numpy as np 
import sklearn
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")
mydata=pd.DataFrame(data)

print(mydata.head())
mydata=mydata.drop(['Unnamed: 5'],axis=1)
mydata=mydata.drop(['Time'],axis=1)


print(mydata)
