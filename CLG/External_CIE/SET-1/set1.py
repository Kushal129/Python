import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dif = {
#     "En_no": [100, 200, 300, 400, 500],
#     "Fop": [80, 71, 90, 40, 60],
#     "Dbms": [82, 92, 75, 78, 88],
#     "cfo": [80, 70, 95, 58, 65],
#     "Maths": [20,18,38,23,23],
#     "Pc": [80, 82, 90, 70, 90]
# }

# df = pd.DataFrame(dif)
# df.to_csv("Marks.csv" , index = False)
# print(df)

df = pd.read_csv('StudentAttendance.csv')
print(df)

# 1. Based on “NumberOfLecturePresent” column add “TotalAbsent” column in data frame. Consider 
# Total conducted lectures 120. 
total_lectures = 120
df['TotalAbsent'] = total_lectures - df['NumberOfLecturePresent']

# 2. Calculate “Absent Percentage” based on “TotalAbsent” column, and add “AbsentPercentage” 
# column in data frame.

df['AbsentPercentage'] = (df['TotalAbsent'] / total_lectures) * 100


# 3. Add the “Eligibility” column, which stores the values  like  “Allowed” or “Not Allowed” based on 
# the given criteria:
#     If Absent percentage grater then 20, then eligibility is “Allowed” else “Not Allowed”.

# 1 -  normal condition
# df['Eligibility'] = ['Allowed' if x <= 20 else 'Not Allowed' for x in df['AbsentPercentage']]

# 2 - using numpy
print()
df['Eligibility'] = np.where(df['AbsentPercentage'] <= 20 , 'Allowed','Not Allowed')
print(df)

# 4. Print the names of top five the student who has highest absent percentage.

top_five_std = df.nlargest(5,'AbsentPercentage')
print('--------------------------------------------------')
print("Top 5 Studnt Highest Absent Percentage")
print('--------------------------------------------------')

print(top_five_std[['StudentName', 'AbsentPercentage']])
print()

#5. Count total number of students who are not allowed to give exam. 

not_allowed_count = len(df[df['Eligibility'] == 'Not Allowed' ] )
print(f"Total Number Of Student Not Allowed To Give The Exam: {not_allowed_count}")
print()

# 6. Display a pie chart that shows the ratio of “allowed” and “not allowed” students
eligibility_count = df['Eligibility'].value_counts()
plt.pie(eligibility_count,labels=eligibility_count.index,autopct='%1.1f%%',startangle=90)
plt.title('Eligibility')
plt.show()

# 7. Store the updated csv file as result.csv
df.to_csv('result.csv',index=False)