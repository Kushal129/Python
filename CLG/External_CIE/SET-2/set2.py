import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('InternalMarks.csv')
print(df)
print()

# 1. To  calculate  final  total internal  marks  out  of  40,  consider  the  following  conversion  criteria.  Add 
# all the converted marks columns i.e. “INT-15,    QZ1-5,    QZ2-5,    UT-8,     ASSIGN-7“. 
# • Convert given Internal exam mark out of 60 into 15 marks.  
# • Convert given Quiz – 1 mark out of 15 into 5 marks.   
# • Convert given Quiz – 2 mark out of 15 into 5 marks. 
# • Convert given unit test mark out of 30 into 8.  
# • Convert given assignment mark out of 10 into 7 marks. 

df['INT-15'] = (df['INT-60'] / 60 ) * 15
df['QZ1-5'] = (df['QZ1-15'] /15 ) * 5
df['QZ2-5'] = (df['QZ2-15'] /15 ) * 5
df['UT-8'] = (df['UT-30'] / 30) * 8
df['ASSIGN-7'] = (df['ASSIGN-10'] / 10) * 7


# 2. Add “Total(40)” column which store sum of all the converted marks.
# axis=0 = columns
# axis=1 = Row 
df['Total(40)'] = df[['INT-15', 'QZ1-5', 'QZ2-5', 'UT-8', 'ASSIGN-7']].sum(axis=1)
print("Adding Total (40)")
print(df)
print()


# 3 .Add the “Result” column, which stores the result of the student. The result will be considered 
# based on the given criteria: 
# • If the student scores less than 16 marks then store the result “FAIL” else store “PASS”

df['Result'] = df['Total(40)'].apply(lambda x: 'PASS' if x >= 16 else 'FAIL')
print('Adding Result')
print(df)
print()

#4. Print name and enrolment of the student who secured highest internal marks
highest_scoring_std = df[df['Total(40)'] == df['Total(40)'].max()]
print("Studnt With Highest Internal Marks:")
print(df)
print()

# 5. Print average internal marks. (Average of Total(40) column.
average_internal_marks = df['Total(40)'].mean()
print(f"Average Internal Marks : {average_internal_marks: .2f}")
print()

# 6. Display a pie chart that shows the ratio of “PASS” and “FAIL” students in final internal.
result_counts = df['Result'].value_counts()
plt.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Result Distribution')
plt.show()

# 7. Store the updated csv file as result.csv.
try:
    df.to_csv('resultset_2.csv', index=False)
    print("DataFrame saved as resultset_2.csv")
    print()
except Exception as e:
    print(f"Error: {e}. DataFrame not saved.")