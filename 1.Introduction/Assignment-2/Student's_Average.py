first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

grades = []

for i in range(3):
    grade = float(input(f"Enter the grade for course {i+1}: "))
    grades.append(grade)

average_grade = sum(grades) / len(grades)
print(average_grade)