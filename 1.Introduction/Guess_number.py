import random

Secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < Secret_number:
            print("Too low! Try again.")
        elif guess > Secret_number:
            print("Too high! Try again")
        else:
            print(f"Congragulations! You've guessed the right number: '{Secret_number}' in {attempts} attempts! ")
    except ValueError:
        print("Please enter a valid number.")