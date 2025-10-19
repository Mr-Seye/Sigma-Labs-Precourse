'''
Coin Toss Betting Game
'''

from random import randint


def get_bet(balance):
    bet_amount = int(input("How much would you like to bet? "))
    if bet_amount > balance:
        print("You do not have enough money to place this bet.")
    else:
        balance -= bet_amount
        return bet_amount, balance


def coin_toss():
    random_num = randint(0, 99)
    if random_num <= 49:
        outcome = "Heads"
    else:
        outcome = "Tails"
    return outcome


def get_choice():
    flip_choice = input(
        "To bet on the coin toss choose either heads or tails: ").strip().lower()
    if flip_choice in ("heads", "h", "tails", "t"):
        settle()
    else:
        print("Invalid input.")


def settle(balance, flip_choice, outcome, bet_amount):
    if flip_choice.lower() == outcome.lower():
        balance += bet_amount * (3/2)
        print(f"You won {bet_amount * (3/2)}! \nYour balance is £{balance}")
    else:
        print(f"You lost £{bet_amount}! \nYour balance is £{balance}.")


balance = 100

print(
    f"Welcome to the coin toss game! \nThis game pays out 3/2 \nYour current balance is £{balance}. ")

is_playing = input("Would you like to play? ").strip().lower()

if is_playing in ("yes", "y"):
    get_bet(get_choice())

elif is_playing == ("no", "n"):
    quit

else:
    print("Invalid input.")
