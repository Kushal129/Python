import numpy as np
import pandas as pd

df = pd.read_csv('Production.csv')

print(df)

#max production
print ("Max Production :",df['Production'].max())
#min production
print ("Min Production :",df['Production'].min())

# production 0
print(df[df['Production']==0])

# 2nd highest production
print("Second heighest production :",df['Production'].nlargest(2).iloc[-1]) 
# iloc[-1]) indexer is used to access the last value of the two largest values found in the previous step

# 3rd  minimum labor hours
print("3rd  minimum labor hours :",df['Labor_Hours'].nsmallest(3).iloc[-1])

# report of labor hour
print(df['Labor_Hours'].describe())

df.insert(5,'Last','NaN')
print(df)

print("Sum Productions :",df['Production'].sum())
print("Avg Productions :",df['Production'].mean())
print("Sum Labor Hours :",df['Labor_Hours'].sum())
print("Avg Labor Hours :",df['Labor_Hours'].mean())
df.to_csv('result2.csv')
