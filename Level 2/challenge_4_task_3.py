animals = [{"name": "Fluffy", "type": "dog"},
           {"name": "Parsley", "type": "dog"},
           {"name": "Ginger", "type": "cat"},
           {"name": "Biscuit", "type": "cat"},
           {"name": "Poppet", "type": "cow"}]


def say_hello_to_my_pets(pets):
    for pet in pets:
        hello_message = ""
        if pet["type"] not in ("cat", "dog"):
            raise Exception("Sorry, only cats and dogs allowed.")
        else:
            if pet["type"] == "dog":
                hello_message = "Woof"
                pet_name = pet["name"]
            if pet["type"] == "cat":
                hello_message = "Meow"
                pet_name = pet["name"]
            print(f"{hello_message}, {pet_name}!")


if __name__ == "__main__":
    say_hello_to_my_pets(animals)
