choices=['rock','paper','scissors']

player=input('choose rock,paper,or scissors').lower()
computer=random.choice(choices)

print(f"computer chose:{computer}")

if player ==computer:
    print("it's a tie!")
elif player == "rock" and computer == "scissors":
    print("you win!Rock beats scissors")
elif player =="paper"and computer == "rock":
    print("you win!Paper beats rock")
elif player == "scissors" and computer == "paper":
    print("you win!Scissors beats paper")
else:
    print("you lose!")

