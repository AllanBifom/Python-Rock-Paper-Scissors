import random
# Allan Bifom
# Python Game
computer_score = 0
player_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("pick Rock/Paper/Scissors")
        continue

    # rock = 0, paper = 1, scissors = 2
    rand_number = random.randint(0, 2)
    computer_choice = options[rand_number]
    print("computer picked",computer_choice )

    if (user_input == "rock" and computer_choice == "scissors") or (user_input == "paper" and computer_choice =="rock") or (user_input == "scissors" and computer_choice =="paper"):
        player_score += 1
        print("You won this round!")
    elif user_input == computer_choice:
        print ("you tie this round")
    else:
        computer_score += 1
        print("you lose this round :(.")


if player_score > computer_score:
    print("Hurray! you win by", str(player_score), "-", str(computer_score) + ".")
else:
    print("ouch, you lose by", str(computer_score), "-", str(player_score) + ".")

print("GameOver!")