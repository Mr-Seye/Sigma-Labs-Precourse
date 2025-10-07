animals = [{"name": "Fluffy", "type": "dog"},
           {"name": "Parsley", "type": "dog"},
           {"name": "Ginger", "type": "cat"},
           {"name": "Biscuit", "type": "cat"},]


def say_hello_to_my_pets(pets):
    for pet in pets:
        hello_message = ""
        if pet["type"] == "dog":
            hello_message = "Woof"
            pet_name = pet["name"] 
        if pet["type"] == "cat":
            hello_message = "Meow"
            pet_name = pet["name"]
        print(f"{hello_message}, {pet_name}!")


if __name__ == "__main__":
    say_hello_to_my_pets(animals)


'''
Order of raised issues:

Initial 'dict' has no attribute 'name'
FIXED by changing pet_name == pet.name -> pet_name == pet["name"]

Second issue was that there were semi-colons in place of colons
at the start of where indentation blocks began
FIXED by changing them to the syntactically correct character (colon)

Third issue is the loop only greets biscuit (last pet in the list)
FIXED by moving the print statement indentation inside the loop as it only prints once the 
loop is finished and since nothing is being stored with each iteration it 
only prints the last held value which is biscuit

'''
