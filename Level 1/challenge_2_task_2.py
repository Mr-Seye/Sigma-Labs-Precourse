# Task 2: Random Username Generator


# Imports for the random username generation
import random
import string

# (1)

#FUNCtions

def reverse_name(name):
  return name[::-1]  # uses the reverse slice to reverse the string


def intersperse_name(surname, reversed_first):
  result = []
  for i in range(max(len(surname), len(reversed_first))): # checks to see which name is longer (the names will only be interspersed as long as there are enough characters in both names)
    if i < len(reversed_first): # essentially a check to see if there are enought characters left to intersperse if not only the name with remaining characters will be reached
      result.append(reversed_first[i])
    if i < len(surname):
      result.append(surname[i])
  return "".join(result) # this results in a list of characters so we join them to form a string again here

def format_name(interspersed): 
  half = len(interspersed) // 2 # floor divison as we cannot have fractional string characters
  first_half = interspersed[:half].capitalize() # slice the names to form halves
  second_half = interspersed[half:].capitalize()
  return f"{first_half} {second_half}" # return these values

# Program (Task 2)

'''
Debugging

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

# Program menu

option = input("Enter your choice here: ")
if option == "1": # interspersed first and second name username
  first_name = input("Enter your first name: ")
  surname = input("Enter your surname: ")
  reversed_first = reverse_name(first_name)
  interspersed = intersperse_name(surname, reversed_first)
  username = format_name(interspersed)
  print(f"Your username is: {username}")
elif option == "2": # random username generation
  username = format_name(''.join(random.choices(string.ascii_lowercase + string.digits, k=10)))
  print(f"Your random username is: {username}")
else: # input validation
  print("This is not a valid option.")







