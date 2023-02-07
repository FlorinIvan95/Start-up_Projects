import random


def guess_number_game():
    while True:
        print("\nGuess the number game. Good luck!\n")
        try:
            secret_number = random.randint(1, 100)
            number_of_guesses = 0
            guess = ""

            while guess != secret_number:
                number_of_guesses += 1
                guess = int(input("Enter your guess: "))

                if guess < secret_number:
                    print("Too low.")
                elif guess > secret_number:
                    print("Too high.")
                elif guess == secret_number and number_of_guesses == 1:
                    print("You're a lucky person and quess the number in first try!")
                else:
                    print(f"You won in {number_of_guesses} guesses!")
        except ValueError:
            print("You have to choise a number between 1 and 100!")
        print(
            "Do you want to play again? (Type 'Y' for a new game or anything else to EXIT)")
        ans = input().lower()
        if ans != 'y':
            break
    print("Thanks for playing!")


guess_number_game()
