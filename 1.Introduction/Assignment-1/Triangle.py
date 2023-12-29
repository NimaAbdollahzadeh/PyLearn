side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("It is possible to form a triangle with these side lengths.")
else:
    print("It is not possible to form a triangle with these side lengths.")