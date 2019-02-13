import random
random_number = random.randint(1, 10)
guess = input("Enter a number between")

if guess:
    guess = int(guess)
    if 1 <= guess <= 10:
        if random_number == guess:
            print("You guessed correctly!")
        elif guess > random_number:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
else:
    print("You've entered nothing!")
