import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")
elif guess > number:
    print("Too high! Try again.")
else:
    print("Too low! Try again.")

print("The number was:", number)