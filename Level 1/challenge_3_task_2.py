
def ask_for_number(): # ask_for_number funciton with try-except input validation 
  while True:
    user_input = input("Please enter a number: ")
    if user_input.strip() == "": # check for empty string
      print("Error: input cannot be empty.")
      continue
    try:
      num = int(user_input) # attempts to turn input into an int
      return num
    except ValueError:
      print("Error: input must be an integer.") # if invalid an error is thrown
  

# Main program 

num = ask_for_number()

# Sum from 1 to n
sum_to = ((num / 2) * (num + 1))
  
# Sum of multiples of 3 and 5 to n  
multi_total = 0
for n in range(0, num + 1):
  if (n % 3 == 0) or (n % 5 == 0):
    multi_total += n
  
# Product of 1 to n
prod_total = 1
for n in range(1, num + 1):
  prod_total *= n

# user input for each feature
choice = input("Choose between 'sum' for sum of 1 to n, 'multi' for sum of multiples of 3 and 5 from 1 to n or 'prod' for factorial: " )

if choice.lower() == "sum": 
  print(f"The sum of integers from 1 to {num} is: {int(sum_to)}")
elif choice.lower() == "multi":
  print(f"The sum of integers that are multiples of 3 or 5 from 1 to {num} are: {multi_total}")
elif choice.lower() == "prod":
  print(f"The sum of the product of integers from 1 to {num} is: {prod_total}")
else:
  print("Invalid choice.")
