
Database_File = "1.Introduction/Assignment-8/translate.txt"
def read_from_file():
    try:
        global words_bank
        with open(Database_File, "r") as file:
            temp = file.read().split("\n")
            words_bank = []
            for i in range(0, len(temp)-1, 2):
                if i+1 < len(temp):
                    my_dict = {"en": temp[i], "fa": temp[i+1]}
                    words_bank.append(my_dict)
                else:
                    print("Error: Incomplete data in the file.")
                    break
        print(words_bank)
    except FileNotFoundError:
        print("File not existed!")

def write_to_database():
    with open(Database_File, "w") as file:
        for word in words_bank:
            file.write(word["en"]+"\n")
            file.write(word["fa"]+"\n")


def translate_english_to_farsi():
    user_text = input("Enter your english text: ")
    user_words = user_text.split(" ")
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"] :
                print(word["fa"], end =" ")
                break
        else:
            print(user_word, end =" ")

def translate_farsi_to_english():
    user_text = input("Enter your farsi text: ")
    user_words = user_text.split(" ")
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                print(word["en"], end =" ")
                break
        else:
            print(user_word, end =" ")

def add_new_word_to_database():
    english = input("Enter English word: ")
    farsi = input("Enter it's farsi meaning: ")
    new_word = {"en":english, "fa":farsi}
    words_bank.append(new_word)
    print("Dictionary updated successfully!")


def show_menu():
    print("\n\n1- Translate English to Farsi.")
    print("2- Translate Farsi to English.")
    print("3- add a new word to database.")
    print("4- Exit")

def choice():
    global words_bank
    choice = int(input("enter your choice: "))
    if choice == 1:
        translate_english_to_farsi()
    elif choice == 2:
        translate_farsi_to_english()
    elif choice == 3:
        add_new_word_to_database()
    elif choice == 4:
        write_to_database()
        print("Goodbye... !")
        exit(0)

if __name__ == "__main__":
    read_from_file()
    while True:
        show_menu()
        choice()