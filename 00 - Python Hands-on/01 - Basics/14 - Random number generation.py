import random

number = random.randint(1, 6)

print(number)

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3","4","5","6","7","8","9","10","J","Q","K","A"]

number = random.randint(low, high)
print(number)

number = random.random()
print(number)

print(options)
option = random.choice(options)
print(option)

print(cards)
random.shuffle(cards)
print(cards)

###Guessing game

guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input("Guess the number! Enter a number between (1 - 100): "))
    guesses += 1

    if guesses > 0:
        print(f"This is your guess number {str(guesses)}, don't give up!")

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"Congratulations! You are correct! The number is {number}")
        break

print(f"This round you took {guesses} guesses, congratulations!")



