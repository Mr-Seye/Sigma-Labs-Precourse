import random


def guess():
    guess_attempts = 0
    user_guess = None
    prev_guess = None
    while user_guess != secret_num:
        user_guess = int(
            input(f"Attempt number {guess_attempts + 1}: Please enter a guess: "))
        if user_guess == prev_guess:
            print(
                f"Attempt number {guess_attempts}: You've already guessed this number, please try another number.")
        elif user_guess > secret_num:
            guess_attempts += 1
            print(
                f"Your guess of {user_guess} is too large.")
            prev_guess = user_guess
        elif user_guess < secret_num:
            guess_attempts += 1
            print(
                f"Your guess of {user_guess} is too small.")
            prev_guess = user_guess
        elif user_guess == secret_num:
            guess_attempts += 1
            if guess_attempts == 0:
                print(
                    f"You win! The secret number was {secret_num} and you guessed it in {guess_attempts + 1} attempt!")
            elif guess_attempts > 1:
                print(
                    f"You win! The secret number was {secret_num} and you guessed it in {guess_attempts} attempts!")


playing = True
print("Would you like to play a guessing game?")

while playing == True:
    opt = input("Type 'p' to play or 'q' to quit. ")
    if opt == "p":
        secret_num = random.randint(1, 100)
        print(secret_num)
        guess()
    elif opt == "q":
        playing = False
    else:
        print("Invalid input.")
