# Write a program to input marks of 5 subjects of a student and display the
# total marksscored,percentagescoredandtheclassofresult.
# Resultcriteria:
# Percentage>=70%:Distinction
# Percentage>=60%and<70%:FirstClass
# Percentage>=50%and<60%:SecondClass
# Percentage>=40%and<50%:PassClass
# Percentage<40%:Fail

def cal_pr(total_marks, max_marks):
    return (total_marks / max_marks) * 100

def result(percentage):
    if percentage >= 70:
        return "Distinction"
    elif 60 <= percentage < 70:
        return "First Class"
    elif 50 <= percentage < 60:
        return "Second Class"
    elif 40 <= percentage < 50:
        return "Pass Class"
    else:
        return "Fail"

# Input marks for 5 subjects
subject_marks = [float(input(f"Enter marks for subject {i + 1}: ")) for i in range(5)]

# Calculate total marks
total_marks = sum(subject_marks)

# Calculate percentage scored
percentage = cal_pr(total_marks, 5 * 100)

# Determine class of result
class_of_result = result(percentage)

# Output
print("  ")
print("=============== RESULT ================")
print(f"Total Marks Scored: {total_marks}")
print("--------------------------------------")
print(f"Percentage Scored: {percentage:.2f}%") 
#:.2f is a formatting specifier that controls how the floating-point number
print("--------------------------------------")
print(f"Class of Result: {class_of_result}")
print("=======================================")

