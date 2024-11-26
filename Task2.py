import random

def main():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    print("Try to guess it!")

    while not guessed_correctly:
        try:
            # Prompt the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempt count

            # Compare the guess to the random number
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {random_number} correctly.")
                print(f"It took you {attempts} attempts.")

        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()