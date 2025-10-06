def print_dict(people):
    for person in people:
        print(
            f"Name: {person['name']}\n"
            f"Age: {person['age']}\n"
            f"Employed: {'Yes' if person['employed'] else 'No'}\n"
        )


def ask_action():
    while True:
        print("What would you like to do?")
        prompt = input(
            "Please enter either 'add', 'remove' or 'quit': ").strip().lower()
        if prompt in ("add", "remove", "quit"):
            return prompt
        print("Invalid input.")


def add_person(people):
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

    person = {"name": new_name, "age": new_age, "employed": is_employed}
    people.append(person)

    print("Person added successfully!\n")
    print_dict(people)


def remove_person(people):
    target = input("Please choose a person to remove: ").strip().lower()
    for person in people:
        if person['name'].lower() == target:
            people.remove(person)
            print(f"{person['name']} has been removed\n")
            print_dict(people)
            break
    else:
        print("Person not found.\n")


def main():
    people = [{'name': "Jane Doe", 'age': 42, 'employed': True},
              {'name': "Tom Smith", 'age': 18, 'employed': True},
              {'name': "Mariam Coulter", 'age': 66, 'employed': False},
              {'name': "Gregory Tims", 'age': 8, 'employed': False}]

    print_dict(people)

    while True:
        act = ask_action()
        if act == "add":
            add_person(people)
        elif act == "remove":
            remove_person(people)
        elif act == "quit":
            break


main()
