import pandas as pd

df=pd.read_csv()

print(df)

df['totalabsent']=120-df['totalpresent']
df['absentper']=df['totalabsent']/120*100

df['quz5']=df['que(15)']/5
df['internal']=df['internal(15)']/15
print(df['quz5'])

hig = df[df['internalmarks'].nlargest()]['name'],['enro'].tolist()

print(hig)



