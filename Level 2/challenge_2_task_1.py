import random

# function to validate the user's choice input
def get_user_opt():
    while True:
        opt = input("Type 'p' to play or 'q' to quit: ").lower()
        if opt in ('p' or 'q'):
            return opt
        print("Input is invalid, please type 'p' or 'q'.")

# function that generates a new random number when called
def generate_secret_num():
    return random.randint(1, 100)

# function that asks the user for their guess and then returns it
def get_user_guess(attempt):
    while True:
        guess = int(
            input(f"Attempt number {attempt}: Please enter your guess: "))
        return guess

''' 
function that evaluates the user's guess and then compares it with the 
secret number
'''
def eval_guess(user_guess, secret_num):
    if user_guess > secret_num:
        return f"Your guess of {user_guess} is too large.", False
    elif user_guess < secret_num:
        return f"Your guess of {user_guess} is too small.", False
    else:
        return f"You guessed correctly! The secret number was {secret_num}.", True

# function that initialises the main game
def play_game():
    secret_num = generate_secret_num()
    # print(f"[DEBUG] Secret number is: {secret_num}")

    guess_attempts = 0
    prev_guess = None

    while True:
        user_guess = get_user_guess(guess_attempts + 1)
        if user_guess == prev_guess:
            print("You've already guessed this number, try another.")
            continue

        guess_attempts += 1
        prev_guess = user_guess

        message, correct = eval_guess(user_guess, secret_num)
        print(message)

        if correct:
            if guess_attempts == 1:
                print(f"You win! You guessed it in {guess_attempts} attempt!")
            else:
                print(f"You win! You guessed it in {guess_attempts} attempts!")
            break

# main function, is essentially the menu
def main():

    print("Would you like to play a guessing game?")
    while True:
        opt = get_user_opt()
        if opt == 'p':
            play_game()
        elif opt == 'q':
            break


main()
