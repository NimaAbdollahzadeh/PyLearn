first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

grades = []
for i in range(3):
    grade = float(input(f"Enter the grade for course {i+1}: "))
    grades.append(grade)

average_grade = sum(grades) / len(grades)

if average_grade >= 17:
    status = "دانشجوی ممتاز"
elif 17 > average_grade >= 12:
    status = "دانشجوی عادی"
elif average_grade < 12:
    status = "دانشجوی مشروط"

print(f"Student: {first_name} {last_name}")
print(f"Average Grade: {average_grade:.2f}")