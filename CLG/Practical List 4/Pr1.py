import pandas as pd

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


df = pd.read_csv('Marks.csv')

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

def calculate_class(percentage):
    if percentage < 40:
        return "KT [1500₹]"
    elif 40 <= percentage < 50:
        return "PASS"
    elif 50 <= percentage < 60:
        return "SECOND"
    elif 60 <= percentage < 70:
        return "FIRST"
    else:
        return "DISTINCTION"


df['Total'] = df['Fop'] + df['Dbms'] + df['cfo'] + df['Maths'] + df['Pc']

df['Pre'] = df['Total'] / 5

df['FOP_GRADE'] = df['Fop'].apply(calculate_grade)
df['DBMS_GRADE'] = df['Dbms'].apply(calculate_grade)
df['CFO_GRADE'] = df['cfo'].apply(calculate_grade)
df['MATHS_GRADE'] = df['Maths'].apply(calculate_grade)
df['PC_GRADE'] = df['Pc'].apply(calculate_grade)

df['Class'] = df['Pre'].apply(calculate_class)

df.to_csv('Marks.csv', index=False)

print(df)
