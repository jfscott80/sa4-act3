number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? " ))
i = 4
while guess != number:
    i -= 1
    if guess == 'q' or i == 0:
        print(f"Sorry! The number was {number}.")
        break
    try:
        guess = int(input(f"That's not the number. You have {i} guesses left. Guess again or press (q) to quit: "))
    except:
        print(f"Sorry! The number was {number}.")
        break
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

if guess == number:
    print("Congratulations! You guessed the right number.")

