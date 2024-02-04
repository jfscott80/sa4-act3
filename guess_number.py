number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of?" ))

while guess != number:
    guess = input("That's not the number. Guess again or press (q) to quit: ")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
if guess == number:
    print("Congratulations! You guessed the right number.")

