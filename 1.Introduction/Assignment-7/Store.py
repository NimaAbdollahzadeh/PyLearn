
Database_File = "1.Introduction/Assignment-7/Database.txt"
PRODUCTS = []

def read_from_database():
    try:
        with open(Database_File, "r") as file:
            for line in file:
                code, name, price, quantity = line.strip().split(",")
                product = {"code": code, "name": name, "price": price, "quantity": int(quantity)}
                PRODUCTS.append(product)
    except FileNotFoundError:
        print("Database file not found. Creating a new one.")
        write_to_database()

def write_to_database():
    with open(Database_File, "w") as file:
        for product in PRODUCTS:
            line = f"{product['code']},{product['name']},{product['price']},{product['quantity']}\n"
            file.write(line) 
    print("Changes applied successfully!")

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- Exit")

def choice():
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Add()
        elif choice == 2:
            Edit()
        elif choice == 3:
            Remove()
        elif choice == 4:
            Search()
        elif choice == 5:
            Show_list()
        elif choice == 6:
            Buy()
        elif choice == 7:
            Exit()
        else:
            print("Invalid choice. Please enter a number between 1 to 7: ")
    except ValueError:
        print("Invalid input. Please enter a number.")

def Add():
    code = input("Enter code: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")
    
    new_product = {"code": code, "name": name, "price": price, "quantity": quantity}
    PRODUCTS.append(new_product)

def Edit():
    User_input = input("Enter code you want to edit: ")
    for product in PRODUCTS:
        if product['code'] == User_input:
            print('1. Name\n2. Price\n3. Quantity ')  
            User_input2 = int(input("Enter the number of the field you want to edit: "))
            if User_input2 == 1:
                new_name = input("Edit name of product: ")
                product['name'] = new_name
            elif User_input2 == 2:
                new_price = input("Edit price of product: ")
                product['price'] = new_price
            elif User_input2 == 3:
                updated_quantity = int(input("Edit quantity of product: "))
                product['quantity'] = updated_quantity
            print("Information updated successfully!")
            break
    else:
        print("Product not found.")
    

def Remove():   
    User_input = input("Enter code you want to remove: ")
    for product in PRODUCTS:
        if product['code'] == User_input:
            PRODUCTS.remove(product)
            print("Product removed successfully!")
            break
    else:
        print("Product not found.")
        
def Search():
    User_input = input("Type your keyword: ")
    found_products = [product for product in PRODUCTS if User_input in (product["code"], product["name"])]
    if found_products:
        print("code\t\tname\t\tprice")
        for product in found_products:
            print("f{product['code']}\t\t{product['name\t\t{product['price]}")
    else:
        print("No products found.")

def Show_list():
    if PRODUCTS:
        print("code\t\tname\t\tprice")
        for product in PRODUCTS:
            print(f"{product['code']}\t\t{product['name']}\t\t{product['price']}")
    else:
        print("No products in the list.")

def Buy():
    total_cost = 0
    purchased_quantities = {}

    while True:
        User_input = input("Enter code you have decided to buy: ")

        if User_input.lower() == "exit":
            break

        found_product = None
        for product in PRODUCTS:
            if product['code'] == User_input:
                found_product = product
                break

        if found_product:        
            User_input2 = int(input("Enter how many you want? "))
            if product['quantity'] >= User_input2:
                product['quantity'] -= User_input2

                if found_product['code'] in purchased_quantities:
                    purchased_quantities[found_product['code']] += User_input2
                else:
                    purchased_quantities[found_product['code']] = User_input2

                item_cost = User_input2 * float(found_product['price'])
                total_cost += item_cost
                print(f"You just bought {User_input2} {found_product['name']} from the shop! Congratulations.")
                print(f"Item Cost: {item_cost:.2f} toman")
                print(f"Stock available: {found_product['quantity']}")
            else:
                print(f"Sorry, there is not enough {found_product['name']} available in the shop.")
        else:
            print("Product not found.")

        continue_shopping = input("Do you want to continue shopping? (yes/no): ").lower()
        if continue_shopping != 'yes':
            break

    print("\nFinal Factor:")
    for product_code, purchased_quantity in purchased_quantities.items():
        product = next((p for p in PRODUCTS if p['code'] == product_code), None)
        if product:
            item_cost = purchased_quantity * float(product['price'])
            print(f"{product['name']} - Quantity: {purchased_quantity}, Item Cost: ${item_cost:.2f}")
            total_cost += item_cost

    print(f"\nTotal Cost: {total_cost:.2f}")

def Exit():
    write_to_database()
    print("EXiting the program.")
    exit()


if __name__ == "__main__":
    print("Welcome to the shop")
    print("Loading...")
    read_from_database()
    print("Data loaded.")

    while True:
        show_menu()
        choice()
        