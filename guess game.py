import random

def guessing_game():
    number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Guess a number between 1 and 10.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed correctly in {attempts} attempts.")
            break

guessing_game()