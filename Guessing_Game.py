import random
import math
# best way to guess is binary search

top_of_range = input("Give the top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
max_guesses = int(math.log(top_of_range, 2))+1

while max_guesses:
    guesses += 1
    user_guess = input("Make a guess: ")
    max_guesses -= 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        print("You got it in", guesses, "guesses")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
    if (max_guesses == 0):
        print(
            f"You failed \n summary: \n actual number: {random_number} \n max number of guesses: {guesses}")
