def guessing_game():
    number = 6
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Guess the correct number.")

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