'''
Coin Toss Betting Game
'''

from random import randint


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


def coin_toss():
    random_num = randint(0, 99)
    if random_num <= 49:
        outcome = "Heads"
    else:
        outcome = "Tails"
    return outcome


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


def settle(balance, flip_choice, outcome, bet_amount):
    if flip_choice.lower() == outcome.lower():
        winnings = int(bet_amount * 1.5)
        balance += winnings
        print(f"You won £{winnings}! \nThe coin landed on {outcome}.")
    else:
        print(f"You lost £{bet_amount}! \nThe coin landed on {outcome}.")
    print(f"Your balance is now £{balance}")
    return balance


balance = 100
print(
    f"Welcome to the coin toss game! \nThis game pays out 3 to 2. \nYour starting balance is £{balance}. ")

while balance > 0:
    flip_choice = get_choice()
    bet_amount, balance = get_bet(balance)
    outcome = coin_toss()
    balance = settle(balance, flip_choice, outcome, bet_amount)

    again = input("Play again? (y/n) ").strip().lower()
    if again not in ("y", "yes"):
        break

print(
    f"Game over! Your final balance is £{balance}.")
