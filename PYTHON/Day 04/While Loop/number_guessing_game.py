# Number Guessing Game using while loop

import random

# Step 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Step 2: Initialize guess as None
guess = None

print("🎯 Guess the number between 1 and 100!")

# Step 3: Keep looping until the guess is correct
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right.")
