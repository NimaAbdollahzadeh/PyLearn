import random

def generate_unique_array(n):
    if n <= 0:
        return []

    numbers = random.sample(range(1, 1000), n)

    return numbers

array_length = int(input("How many numbers do you want to generate? "))
result_array = generate_unique_array(array_length)
print(result_array)