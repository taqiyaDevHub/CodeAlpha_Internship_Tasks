# CODEALPHA INTERNSHIP TASK#01:  "HANGMAN GAME"

import random

predefined_words = ["strawberry","adventure","astronomy","cauliflower","bouquet"]

hangman = {0: ("\n|---------",
               "|    |    ",
               "|         ",
               "|         ",
               "|         ",
               "|         ",
               " ========="),
           1: ("\n|---------",
               "|    |    ",
               "|    O    ",
               "|         ",
               "|         ",
               "|         ",
               " ========="),
           2: ("\n|---------",
               "|    |    ",
               "|    O    ",
               "|    |    ",
               "|         ",
               "|         ",
               " ========="),
           3: ("\n|---------",
               "|    |    ",
               "|    O    ",
               "|   /|    ",
               "|         ",
               "|         ",
               " ========="),
           4: ("\n|---------",
               "|    |    ",
               "|    O    ",
               "|   /|\\  ",
               "|         ",
               "|         ",
               " ========="),
           5: ("\n|---------",
               "|    |    ",
               "|    O    ",
               "|   /|\\  ",
               "|   /     ",
               "|         ",
               " ========="),
           6: ("|---------",
               "|    |    ",
               "|    O    ",
               "|   /|\\  ",
               "|   / \\  ",
               "|         ",
               " ========="),
            }

def display_man(wrong_guess):
    for line in hangman[wrong_guess]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(correct_answer):
    print(" ".join(correct_answer))

def main():
    correct_answer = random.choice(predefined_words)
    hint = ["_"] * len(correct_answer)
    wrong_guess = 0
    guessed_letters = set()
    running = True

    print("\n======== WELCOME TO THE HANGMAN GAME ========\n")
    
    while running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! \nType a single alphabet.\n")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!\n")
            continue

        guessed_letters.add(guess)

        if guess in correct_answer:
            for i in range(len(correct_answer)):
                if correct_answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1
            print(f"\nWrong guess.. \nAttempts left: {len(hangman)-1 - wrong_guess}\n")

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(correct_answer)
            print("CONGRATULATIONS! YOU WON THE GAME!")
            running = False
        elif wrong_guess >= 6:
            display_man(wrong_guess)
            print("OOPS! THE MAN IS HANGED..\nYOU LOSE!")
            print("\nThe correct word is:")
            display_answer(correct_answer)
            running = False

if __name__ == "__main__":
    main()
