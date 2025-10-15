from datetime import date, datetime


def calc_age(birthdate):
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = date.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


if __name__ == "__main__":
    user_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        age = calc_age(user_input)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
