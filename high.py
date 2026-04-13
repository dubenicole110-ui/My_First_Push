import random
number = random.randint(1,100)
attempt = 0
while True:
    guess = int(input("guess the number between 1 and 100:"))
    attempt += 1
    if guess < number:
        print("too low try again ")
    elif guess > number:
        ptint ("too high try again") 
    else:
        print(f"congratulations! you have guessed the number")
        break   