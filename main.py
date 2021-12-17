import random

choices = ["rock", "paper", "scissor"]

user_name = input("Enter your name: ")
print()
print(f"Hi {user_name.capitalize()}. Welcome to the game.")
print()

user_score = 0
comp_score = 0


times_to_play = int(input("How many times do you want to play : "))
for i in range(times_to_play):
    print()
    user_choice = input("Rock, Paper or Scissor : ").lower()
    comp_choice = random.choice(choices)

    if comp_choice == user_choice:
        print("Draw !!!")

    elif user_choice == "rock" and comp_choice == "paper":
        print()
        print(
            f"Your choice: {user_choice}. \nComputer's choice: {comp_choice}")
        print("Computer won")
        comp_score += 1

    elif user_choice == "paper" and comp_choice == "rock":
        print()
        print(
            f"Your choice: {user_choice}. \nComputer's choice: {comp_choice}")
        print("You won")
        user_score += 1

    elif user_choice == "scissor" and comp_choice == "paper":
        print()
        print(
            f"Your choice: {user_choice}. \nComputer's choice: {comp_choice}")
        print("You won")
        user_score += 1

    elif user_choice == "rock" and comp_choice == "scissor":
        print()
        print(
            f"Your choice: {user_choice}. \nComputer's choice: {comp_choice}")
        print("You won")
        user_score += 1

    elif user_choice == "paper" and comp_choice == "scissor":
        print()
        print(
            f"Your choice: {user_choice}. \nComputer's choice: {comp_choice}")
        print("Computer won")
        comp_score += 1

    else:
        print("Invalid")
