# python3 challenge_1_task_2.py
# Task 2a

# Ask for name input
name = input("What is your name? ")

# print(f"Hello {name}!")

# Task 2b
# Check to see if name is Alice or Bob, if so greet them
if name == "Alice" or name == "Bob":
  print(f"Hello {name}!")
  
# If not print unauthorised message
else:
  print("Sorry... You're not authorised to be greeted!")
