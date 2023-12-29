def remove_duplicate(input_list):
    unique_elements = []
    for item in input_list :
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

user_input = input("Enter numbers seperated with spaces: ")
user_numbers = [int(num) for num in user_input.split()]

result_list = remove_duplicate(user_numbers)
print(result_list)