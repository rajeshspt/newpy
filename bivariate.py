import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-29/Desktop/dataset/water_potability235.csv")
print(data.head(10))
g=sns.countplot(x='ph',hue='Solids',data=data)
print(data)

 
def add_clean(df):
 df['clean']=df['Good'] + df['bad'] +1 
 return df
data=add_clean(data)
data.head(10)
