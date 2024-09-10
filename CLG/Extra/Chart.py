import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the "Marks.csv" file
df = pd.read_csv('Marks.csv')

# I. Add the "Total" column, which stores the total of all the subject marks.
df['Total'] = df[['Fop', 'Dbms', 'cfo', 'Maths', 'Pc']].sum(axis=1)

# Function to calculate grade based on given criteria
def calculate_grade(marks):
    if marks < 40:
        return "FF"
    elif 40 <= marks < 50:
        return "CC"
    elif 50 <= marks < 60:
        return "BC"
    elif 60 <= marks < 70:
        return "AB"
    else:
        return "AA"

# II. Add columns for subject grades
df['FOP_GRADES'] = df['Fop'].apply(calculate_grade)
df['DBMS_GRADES'] = df['Dbms'].apply(calculate_grade)
df['CFO_GRADES'] = df['cfo'].apply(calculate_grade)
df['MATHS_GRADES'] = df['Maths'].apply(calculate_grade)
df['PC_GRADES'] = df['Pc'].apply(calculate_grade)

# III. Add the "Percentage" column
df['Percentage'] = (df['Total'] / 500) * 100

# IV. Add the "Result Class" column based on percentage
def calculate_class(percentage):
    if percentage < 40 or any(df[['Fop', 'Dbms', 'cfo', 'Maths', 'Pc']].min(axis=1) < 40):
        return "FAIL"
    elif 40 <= percentage < 50:
        return "PASS"
    elif 50 <= percentage < 60:
        return "SECOND"
    elif 60 <= percentage < 70:
        return "FIRST"
    else:
        return "DISTINCTION"

df['Result Class'] = df['Percentage'].apply(calculate_class)

# V. Print the name of the student who secured the 1st Rank based on percentage.
top_student = df[df['Percentage'] == df['Percentage'].max()]
print("Student with the highest percentage:")
print(top_student[['Student Name', 'Percentage']])

# VI. Print the name of the student who secured the minimum percentage.
lowest_student = df[df['Percentage'] == df['Percentage'].min()]
print("\nStudent with the lowest percentage:")
print(lowest_student[['Student Name', 'Percentage']])

# VII. Store the updated CSV file as result.csv.
df.to_csv('result.csv', index=False)

# Show a pie chart for the distribution of result classes
result_distribution = df['Result Class'].value_counts()
result_distribution.plot(kind='pie', autopct='%1.1f%%', title='Result Class Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Show a bar chart for the total marks and percentage
df[['Total', 'Percentage']].plot(kind='bar', title='Total Marks and Percentage')
plt.xlabel('Student')
plt.show()
