import math
import mpmath

while True:
    print("+ : sum")
    print("- : sub")
    print("* : mul")
    print("/ : dev")
    print("sin : sin")
    print("cos : cos")
    print("tan : tan")
    print("cot : cot")
    print("factorial : factorial")
    print("sqrt : sqrt")
    print("log : log")
    print("quit")
    print("Please enter a choice: ")

    operator = input()

    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter number: "))
    elif operator =="sin" or operator == "cos" or operator == "tan" or operator == "cot" or operator == "factorial" or operator == "sqrt" or operator == "log": 
        num1 = float(input("Enter number: "))

    if operator == "quit":
        print("Enough calculating! see you later!")
        break

    if operator == "+":
        result = num1 + num2
    
    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2
    
    elif operator == "/":
        result = num1 / num2 
    
    elif operator == "sin":
        degree = math.sin(num1)
        result = degree * (math.pi / 180)
    
    elif operator == "log":
        result = math.log(num1)
    
    elif operator == "cos":
        degree = math.cos(num1)
        result = degree * (math.pi / 180)
    
    elif operator == "tan":
        degree = math.tan(num1)
        result = degree * (math.pi / 180)

    elif operator == "cot":
        degree = mpmath.cot(num1)
        result = degree * (math.pi / 180)
    
    elif operator == "sqrt":
        result = math.sqrt(num1)
    
    elif operator == "factorial":
        result = math.factorial(int(num1))


    print(result)
