def is_factorial_number(number):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    
    current_factorial = 1
    i = 1
    while current_factorial < number :
        i += 1
        current_factorial = factorial(i)

    if current_factorial == number:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))

    is_factorial_number(user_input)