def read_from_database():
    f = open("1.Introduction/Assignment-7/Database.txt", "r")

    for line in f:
        result = line.split(",")
        mydict = {"code" : result[0], "name" : result[1], "price" : result[2], "quantity" : result[3]}
        PRODUCTS.append(mydict)
    
    f.close()

def write_to_database():
    pass


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- Exit")

def choice():
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


def Add():
    code = input("Enter code: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")
    
    new_product = {"code": code, "name": name, "price": price, "quantity": quantity}
    PRODUCTS.append(new_product)

def Edit():
    pass

def Remove():   
    pass

def Search():
    User_input = input("Type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == User_input or product["name"] == User_input:
            print(product["code"],"\t\t", product["name"],"\t\t", product["price"])
            break
    else:
        print(ValueError("Not found!"))

def Show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t", product["name"],"\t", product["price"])

def Buy():
    pass

def Exit():
    write_to_database()


PRODUCTS = list()

print("Welcome to the shop")
print("Loading...")
read_from_database()
print("Data loaded.")
while True:
    show_menu()
    choice()

