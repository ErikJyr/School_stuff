import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
my_action = random.choice(possible_actions)
print (f"\nYou chose {user_action}, I chose {my_action}.\n")
if user_action == my_action:
    print(f"It's a tie!")
elif (user_action == "rock" and my_action == "scissors") or (user_action == "paper" and my_action == "rock") or (user_action == "scissors" and my_action == "paper"):
    print(f"You win!")
else:
    print(f"You lose!")

