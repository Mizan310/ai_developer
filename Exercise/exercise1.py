# Create a Python function where the user has to guess a secret number within 5 tries.

import random

def guessing_number():

    number = random.randint(1, 100)
    guess = 0

    for guess in range(5):
        guess = int(input("Enter the number: "))
        if (guess < number):
            print("Guess higher")
        elif (guess > number):
            print("Guess lower")
        else:
            print("Won the game")

guessing_number()