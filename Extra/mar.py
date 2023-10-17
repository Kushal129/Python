import numpy as np
import pandas as pd

def fop_grade():
               if(df['FOP']<40):
                   return 'FF'
               elif(df['percentage']>=40 and df['percentage']<50):
                   return 'CC'
               elif(df['percentage']>=50 and df['percentage']<60):
                   return 'BC'
               elif(df['percentage']>=60 and df['percentage']<70):
                   return 'AB'
               else:
                   return 'AA'
                
df = pd.read_csv('Marks.csv')

df['total'] = df['FOP']+df['DBMS']+df['CFO']+df['MATHS']+df['PC']
df['percentage'] = (df['total']*100)/500
fop = df['FOP']
df['FOP_GRADE'] = df.apply(fop,axis=1)

print(df)
print("===================================")
second = df.nlargest(1, ['percentage'])

sec = np.array(second)

print("Highest Percentage :",sec[0][1])
print("===================================")
minimum = df.nsmallest(1, ['percentage'])

mini = np.array(minimum)

print("Minimum Percentage :",mini[0][1])

df.to_csv('marksoutput.csv')
