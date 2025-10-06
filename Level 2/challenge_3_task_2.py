
'''
for key, val in people[0].items():
    print(f"Name: {people[]['first_name']}")

print("Do you want to Add or Remove information?")

prompt = input("Type 'Add' or 'Remove': ")
'''


def print_dict():
    for index in range(len(people)):
        for key in people[index]:
            if (key == 'name'):
                print(
                    f"Name: {people[index]['name']} \nAge: {people[index]['age']} \nEmployed: {'Yes' if people[index]['employed'] else 'No'} \n")


def ask_action():
    while True:
        print("What would you like to do?")
        prompt = input(
            "Please enter either 'add', 'remove' or 'quit': ").strip().lower()


def add_person():
    while True:
        new_name = input(
            "Please enter the name of the person you would like to add: ")
        new_age = int(
            input("Please enter the age of the person you are adding: "))
        is_employed = input("Is this person employed? ").strip().lower()
        if is_employed in ("y", "yes", "true", "t", "1"):
            is_employed = True
        elif is_employed in ("n", "no", "false", "f", "0"):
            is_employed = False
        else:
            print("Invalid input.")


def remove_person():
    target = input("Please choose a person to remove: ")
    for i in people:
        if target in people[i]['name']:
            del people[i]
        else:
            print("Person not found.")


def main():
    people = [{'name': "Jane Doe", 'age': 42, 'employed': True},
              {'name': "Tom Smith", 'age': 18, 'employed': True},
              {'name': "Mariam Coulter", 'age': 66, 'employed': False},
              {'name': "Gregory Tims", 'age': 8, 'employed': False}]
    print_dict(people)
    while True:
        act = ask_action
        if act == "add":
            add_person(people)
        elif act == "remove":
            remove_person(people)
        elif act == "quit":
            break

