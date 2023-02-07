import random
import time

print("Welcome to the Rock, Paper, Scissors Game! \nEnjoy!")

while True:
    print("\nEnter your choice: \n1 for Rock \n2 for Paper \n3 for Scissors \n")
    try:
        choice = int(input("Choise: "))

        while choice > 3 or choice < 1:
            choice = int(
                input("You must choose one of the 3 numbers above (1, 2 or 3): "))

        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        elif choice == 3:
            choice_name = 'Scissors'

        print(f"Your choice: {choice_name}")

        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        elif comp_choice == 3:
            comp_choice_name = 'Scissors'

        time.sleep(2)
        print(f"Computer choice: {comp_choice_name}")

        time.sleep(2)
        print(f"{choice_name} Vs {comp_choice_name}")

        result = choice - comp_choice
        time.sleep(2)

        if result == 0:
            print("Draw")
        elif choice == 1 and result == -1:
            print("You lose!", comp_choice_name, "covers", choice_name)
        elif choice == 1 and result == -2:
            print("You win!", choice_name, "smashes", comp_choice_name)
        elif choice == 2 and result == 1:
            print("You win!", choice_name, "covers", comp_choice_name)
        elif choice == 2 and result == -1:
            print("You lose!", comp_choice_name, "cuts", choice_name)
        elif choice == 3 and result == 2:
            print("You lose!", comp_choice_name, "smashes", choice_name)
        elif choice == 3 and result == 1:
            print("You win!", choice_name, "smashes", comp_choice_name)

    except ValueError:
        print("You must choose one of the 3 numbers above (1, 2 or 3)")

    time.sleep(2)
    print("Do you want to play again? (Type 'Y' for a new game or anything else to EXIT)")
    ans = input().lower()
    if ans != 'y':
        break

print("\nThanks for playing!See you again!")
