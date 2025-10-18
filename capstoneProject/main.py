'''
Coin Toss Betting Game
'''

from random import randint

balance = 100

print(
    f"Welcome to the coin toss game! \nThis game pays out 3/2 \nYour current balance is £{balance}. ")

is_playing = input("Would you like to play? ").strip().lower()

if is_playing == "yes":
    bet_amount = int(input("How much would you like to bet? "))
    balance -= bet_amount
    flip_choice = input(
        "To bet on the coin toss choose either heads or tails: ")
    random_num = randint(0, 99)
    if random_num <= 49:
        result = "Heads"
    else:
        result = "Tails"

    if flip_choice.lower() == result.lower():
        balance += bet_amount * (3/2)
        print(f"You won {bet_amount * (3/2)}! \nYour balance is £{balance}")
    else:
        print(f"You lost £{bet_amount}! \nYour balance is £{balance}.")

elif is_playing == "no":
    quit

else:
    print("Invalid input.")
