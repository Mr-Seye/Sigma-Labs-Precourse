# Task 2: Random Username Generator


# Imports for the random username generation
import random
import string

# (1)

#FUNCtions
def reverse_name(name):
  return name[::-1]

def intersperse_name(surname, reversed_first):
  result = []
  for i in range(max(len(surname), len(reversed_first))):
    if i < len(reversed_first):
      result.append(reversed_first[i])
    if i < len(surname):
      result.append(surname[i])
  return "".join(result)

def format_name(interspersed):
  half = len(interspersed) // 2
  first_half = interspersed[:half].capitalize()
  second_half = interspersed[half:].capitalize()
  return f"{first_half} {second_half}"

# Program (Task 2)

'''
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

reversed_first = reverse_name(first_name)
print(f"Reversed first name: {reversed_first}")

interspersed = intersperse_name(surname, reversed_first)
print(f"Interspersed name: {interspersed}")

final_name = format_name(interspersed)
print(f"Formatted name: {final_name}")
'''
# Program (Task 3)

print("Welcome to the username creator!\nPlease choose one of the following options:\n1. Create a username based on a name \n2. Create a random username")

option = input("Enter your choice here: ")
if option == "1":
  first_name = input("Enter your first name: ")
  surname = input("Enter your surname: ")
  reversed_first = reverse_name(first_name)
  interspersed = intersperse_name(surname, reversed_first)
  username = format_name(interspersed)
  print(f"Your username is: {username}")
elif option == "2":
  username = format_name(''.join(random.choices(string.ascii_lowercase + string.digits, k=10)))
  print(f"Your random username is: {username}")
else:
  print("This is not a valid option.")







