number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of?" ))
i = 4
while guess != number:
    i -= 1
    if guess == 'q' or i == 0:
        print(f"Sorry! The number was {number}.")
        break
    guess = input(f"That's not the number. You have {i} guesses left. Guess again or press (q) to quit: ")

if guess == number:
    print("Congratulations! You guessed the right number.")

