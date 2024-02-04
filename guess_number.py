number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != number:
    try:
        guess = int(input("That's not the number. Guess again or press (q) to quit: "))
    except:
        print(f"Sorry! The number was {number}.")
        break
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

if guess == number:
    print("Congratulations! You guessed the right number.")

