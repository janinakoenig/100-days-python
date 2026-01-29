import random

def main():
    print("Welcome to Day 1 - Guessing Game!")
    print("Guess my number between 1 and 100, including both of them!")

    number = random.randint(1, 100)
    guessed = False

    while not guessed:
        print("Enter your guess:")
        guess = int(input())
        if guess == number:
            guessed = True
        elif guess < number:
            print("This wasn't my number :(")
            print("Your number is too small")
        elif guess > number:
            print("This wasn't my number :(")
            print("Your number is too big")

    print("Congrats! You've guessed my number :)")

if __name__ == "__main__":
    main()
