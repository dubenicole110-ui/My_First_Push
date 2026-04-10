choices=['rock','paper','scissors']

player=input('choose rock,paper,or scissors').lower()
computer="random.choice(choices)"

print(f"computer chose:", computer)

if player ==computer:
    print("it's a tie!")
elif player == "rock" and computer == "scissors":
    print("you win!rock beats scissors")
elif player =="paper"and computer == "rock":
    print("you win!paper beats rock")
elif player == "scissors" and computer == "paper":
    print("you win!scissors beats paper")
elif player == "scissors"and computer =="rock":
    print("you win!rock beats scissors")
else:
    print("you lose!")


    