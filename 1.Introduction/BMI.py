height_cm = float(input("Enter your height please: "))
weight_kg = float(input("Enter your weight please: "))
height_m = height_cm / 100
bmi = weight_kg /(height_m ** 2)
if bmi < 18.5:
    category = "Under Weight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
elif 24.9 <= bmi < 29.9:
    category = "Over Weight"
elif 29.9 <= bmi < 34.9:
    category = " Obesity"
elif 24.9 <= bmi < 39.9:
    category = "Extreme Obesity"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")