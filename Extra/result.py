import numpy as np
import pandas as pd

def percentage(df):
               if(df['percentage']<40):
                   return 'FF'
               elif(df['percentage']>=40 and df['percentage']<50):
                   return 'CC'
               elif(df['percentage']>=50 and df['percentage']<60):
                   return 'BB'
               else:
                   return 'AA'


df = pd.read_csv('result.csv')

print(df)

df['total'] = df['q1']+df['q2']+df['q3']
df['percentage'] = (df['total']*100)/30
df['result'] = df.apply(percentage,axis=1)

print(df)

m1=df['q1'].mean()
m2=df['q2'].mean()
m3=df['q3'].mean()

arr = np.array([m1,m2,m3])

min = arr.min()

if(m1==min):
    print('m1')
elif(m2==min):
    print('m2')
elif(m3==min):
    print('m3')
    

first = df.nlargest(1, ['percentage'])

fir = np.array(first)

second = df.nlargest(2, ['percentage'])

sec = np.array(second)

print("First Highest :",sec[0][5])
print("Second Highest :",sec[1][5])

print("Enrollment Number of First Rank : ",sec[0][0])
print("Enrollment Number of Second Rank : ",sec[1][0])
