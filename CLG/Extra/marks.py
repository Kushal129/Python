
import numpy as np
import pandas as pd


def percentage(obj):
   
    if (obj<= 40):
        return "FF"
    elif (obj>40 and obj<50):
        return 'CC'
    elif (obj>50 and obj<60):
        return 'BC'
    elif (obj>60 and obj<70):
        return 'AB'
    elif (obj>40):
        return 'AA'
    
def percentageclass(df):
    if (df['percetnage']<= 40):
        return "FAIL"
    elif (df['percetnage']>40 and df['percetnage']<50):
        return 'PASS'
    elif (df['percetnage']>50 and df['percetnage']<60):
        return 'SECOND'
    elif (df['percetnage']>60 and df['percetnage']<70):
        return 'FIRST'
    elif (df['percetnage']>40):
        return 'DISTINCTION'

df = pd.read_csv('Marks.csv')

print(df)
#Add Total Colun at the end 
df['total'] = df['FOP']+df['DBMS']+df['CFO']+df['MATHS']+df['PC']
print(df)


# Calculate for all subject weather student is pass in every subject or not 
df['FOP_GRADS'] = df['FOP'].apply(percentage)
df['DBMS_GRADS'] = df['DBMS'].apply(percentage)
df['CFO_GRADS'] = df['CFO'].apply(percentage)
df['MATHS_GRADS'] = df['MATHS'].apply(percentage)
df['PC_GRADS'] = df['PC'].apply(percentage)


# percentage of all students
df['percetnage']=(df['total'])*100/500

df['result'] =df.apply(percentageclass,axis=1)

# 1st rank
print ("1st Rank :",df['percentage'].max())
print ("minimum percentage :",df['percentage'].min())
df.to_csv('result.csv')

