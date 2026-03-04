# INTERNSHIP TASK#01:  "HANGMAN GAME"

import random

predefined_words = ["strawberry","adventure","astronomy","cauliflower","bouquet"]

hangman = {0: ("|---------",
               "|    |    ",
               "|         ",
               "|         ",
               "|         ",
               "|         ",
               " ========="),
           1: ("|---------",
               "|    |    ",
               "|    O    ",
               "|         ",
               "|         ",
               "|         ",
               " ========="),
           2: ("|---------",
               "|    |    ",
               "|    O    ",
               "|    |    ",
               "|         ",
               "|         ",
               " ========="),
           3: ("|---------",
               "|    |    ",
               "|    O    ",
               "|   /|    ",
               "|         ",
               "|         ",
               " ========="),
           4: ("|---------",
               "|    |    ",
               "|    O    ",
               "|   /|\\  ",
               "|         ",
               "|         ",
               " ========="),
           5: ("|---------",
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
            print(f"Wrong guess.. \nAttempts left: {len(hangman)-1 - wrong_guess}\n")

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(correct_answer)
            print("CONGRATULATIONS! YOU WON THE GAME!")
            running = False
        elif wrong_guess >= 6:
            display_man(wrong_guess)
            print("OOPS! THE MAN IS HANGED..\nYOU LOSE!")
            print("Correct word is:")
            display_answer(correct_answer)
            running = False

if __name__ == "__main__":
    main()
