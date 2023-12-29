import random

def choose_word():
    words = ["elephant", "computer", "sunshine", "chocolate", "butterfly", "mountain", "keyboard", "adventure", "strawberry", "happiness", "christmas", "guitar", "watermelon", "rainbow", "universe", "vacation", "eiffel tower", "friendship", "basketball", "beach", "fireworks", "halloween", "ice cream", "lighthouse", "waterfall"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Wrong guess!")

        if attempts == 0:
            print("Sorry, your're out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()