import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cie.csv') 

# 1. Add columns “FOP-1(15), FOP-2(15), FOP-3(20), DBMS-1(15), DBMS-2(15), DBMS-3(20)”. 
# Calculate and store the marks based on the individual CIE marks. 
# • FOP and DBMS – CIE – 1 (30) convert into 15 marks. 
# • FOP and DBMS – CIE – 2 (30) convert into 15 marks. 
# • FOP and DBMS – CIE – 3 (30) convert into 20 marks. 

df['FOP-1(15)'] = (df['FOP-1(15)'] /30 ) * 15
df['FOP-2(15)'] = (df['FOP-2(15)'] /30 ) * 15
df['FOP-3(15)'] = (df['FOP-3(20)'] /30 ) * 20
df['DBMS-1(15)'] = (df['DBMS-1(15)'] /30 ) * 15
df['DBMS-2(15)'] = (df['DBMS-2(15)'] /30 ) * 15
df['DBMS-3(20)'] = (df['DBMS-3(20)'] /30 ) * 20

print(df)
print()

# 2 .Add columns “FOP Total, DBMS Total”.  Calculate and store total marks into each column based 
# on following: 
# • FOP Total = FOP-1(15) + FOP-2(15) + FOP-3(20) 
# • DBMS Total = DBMS-1(15) + DBMS-2(15) + DBMS-3(20)

df['FOP Total'] = df[['FOP-1(15)' , 'FOP-2(15)' , 'FOP-3(20)']].sum(axis=1)
df['DBMS Total'] = df[['DBMS-1(15)' , 'DBMS-2(15)' , 'DBMS-3(20)']].sum(axis=1)
print(df)
print()

# 3. Add the “Percentage” column, which stores the percentage based on two subject total marks

df['Percentage'] = (df['FOP Total'] + df['DBMS Total']) / 2

#4. Print the names of the student who secured the 1st Rank based on percentage.
first_rank_std = df[df['Percentage'] == df['Percentage'].max()]
print("Student With 1st Rank: ")
print(first_rank_std[['StudentName' , 'Enrollment']])
print()

# 5 .Add the “Result  Class” column, which stores the result of the student. The result will be 
# considered based on the given criteria: 
# • If the student scores less than 50 marks in any subject or the percentage is less than 50, 
# store the result “FAIL”. 
# • If the percentage is between 50 to 60, then store result “SECOND”. 
# • If the percentage is between 60 to 70, then store result “FIRST”. 
# • If the percentage is greater than 70, then store result “DISTINCTION”

def classify_result(row):
    if row['FOP Total'] < 50 or row['DBMS Total'] < 50 or row['Percentage'] < 50:
        return 'FAIL'
    elif row['Percentage'] < 60:
        return 'SECOND'
    elif row['Percentage'] < 70:
        return 'FIRST'
    else:
        return 'DISTINCTION'

df['Result Class'] = df.apply(classify_result, axis=1)
print(df)
print()

# 6 . Display a bar chart by grouping the classes given in “Result Class” column. 
result_class_counts = df['Result Class'].value_counts()
result_class_counts.plot(kind='bar', color=['red', 'orange', 'green', 'blue'])
plt.title('Result Class Distribution')
plt.xlabel('Result Class')
plt.ylabel('Number of Students')
plt.show()

# 7 .Store the updated csv file as result.csv. 
df.to_csv('resultset1_1.csv' , index=False)
