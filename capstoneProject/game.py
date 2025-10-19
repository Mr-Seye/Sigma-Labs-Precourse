'''
Coin Toss Betting Game
'''

# random module for the coin flip
from random import randint


# function to get the inputs required to place a bet amount
def get_bet(balance):
    while True:
        try:
            bet_amount = int(input("How much would you like to bet? "))
            if bet_amount <= 0:
                print("Bet must be greater than £0.")
            elif bet_amount > balance:
                print("You do not have enough money for that bet.")
            else:
                balance -= bet_amount
                return bet_amount, balance
        except ValueError:
            print("Please enter a valid integer.")

# function to 'simulate' a coin toss (essentially just a 50/50 random number generator)


def coin_toss():
    random_num = randint(0, 99)
    if random_num <= 49:
        outcome = "Heads"
    else:
        outcome = "Tails"
    return outcome


# function to get the user's outcome prediction
def get_choice():
    while True:
        flip_choice = input(
            "To bet on the coin toss choose either heads or tails: ").strip().lower()
        if flip_choice in ("heads", "h"):
            return "Heads"
        elif flip_choice in ("tails", "t"):
            return "Tails"
        else:
            print("Invalid input. Please type 'heads' or 'tails'.")

# function to settle the outcome of the bet, award winnings and relay this information


def settle(balance, flip_choice, outcome, bet_amount):
    if flip_choice.lower() == outcome.lower():
        winnings = int(bet_amount * 1.5)
        balance += winnings
        print(f"You won £{winnings}! \nThe coin landed on {outcome}.")
        print(f"Your balance is now £{balance}")
        return balance, "win"
    else:
        print(f"You lost £{bet_amount}! \nThe coin landed on {outcome}.")
        print(f"Your balance is now £{balance}")
        return balance, "loss"


# initialised values for tracking
balance = 100
rounds_played = 0
wins = 0
losses = 0

print(
    f"Welcome to the coin toss game! \nThis game pays out 3 to 2. \nYour starting balance is £{balance}. ")

# main program loop
while balance > 0:
    flip_choice = get_choice()
    bet_amount, balance = get_bet(balance)
    outcome = coin_toss()
    balance, result = settle(balance, flip_choice, outcome, bet_amount)

    rounds_played += 1
    if result == "win":
        wins += 1
    else:
        losses += 1

    print(f"Rounds played: {rounds_played}")
    again = input("Play again? (y/n) ").strip().lower()
    if again not in ("y", "yes"):
        break

print(
    f"\nGame over! You played {rounds_played} round(s): {wins} win(s), {losses} loss(es).\nYour final balance is £{balance}.")
