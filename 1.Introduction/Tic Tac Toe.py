import pyfiglet
import time
from termcolor import colored
import random

def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(colored("X", "red"), end=" ")  
            elif cell == "O":
                print(colored("O", "blue"), end=" ")  
            else:
                print(colored("-", "yellow"), end=" ")
        print()

def player_input(player):
    while True:
        try:
            row = int(input(f"{player}: Enter a row (0-2): "))
            col = int(input("{player}: Enter a column (0-2): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue 
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-":
                return row, col
            else:
                print("That space is already filled. Try again.")
        else:
            print("Number out of list range. Try again!")

def CPU():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if game_board[row][col] == "-":
            time.sleep(1)
            return row, col
        
def update_board(row, col, player):
    game_board[row][col] = player

def check_game():
    for player in ["X", "O"]:
        if any(all(cell == player for cell in row) for row in game_board) or \
           any(all(game_board[row][col] == player for row in range(3)) for col in range(3)) or\
           all(game_board[i][i] == player for i in range(3)) or\
           all(game_board[i][2 - i] == player for i in range(3)):
            print(f"Player {player} wins!")
            return True
    
    if all(all(cell != "-" for cell in row) for row in game_board):
        print("It's a draw!")
        return True

    return False

def main_menu():
    print("1: Player1 vs Player2")
    print("2: Player1 vs CPU")
    choice = int(input("Enter your choice (1 o 2): "))
    if choice == 1:
        show()
        while True:
            row, col = player_input("X")
            update_board(row, col, "X")
            show()
            if check_game():
                break
            row, col = player_input("O")
            update_board(row, col, "O")
            show()
            if check_game():
                break
        
    elif choice == 2:
        show()
        while True:
            row, col = player_input("X")
            update_board(row, col, "X")
            show()
            if check_game():
                break
            row, col = CPU()
            update_board(row, col, "O")
            show()
            if check_game():
                break
            

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]


start_time = time.time()
main_menu()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"time spent: {elapsed_time:.2f} seconds")