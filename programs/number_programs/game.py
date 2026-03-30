import random
choices = ["rock", "paper", "scissors"]
while True:
    user = input("Enter rock/paper/scissors (or quit): ")
    
    if user == "quit":
        break
    
    comp = random.choice(choices)
    print("Computer:", comp)

    if user == comp:
        print("Draw")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("You lose!")