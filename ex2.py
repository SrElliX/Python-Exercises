# Exercises in Python

# create a program that asks the user to enter an integer, inform whether this number is an even or odd number, if the user does not enter an integer, inform that it is not an integer

print('Find out if a number is even or odd!') # Tells you what the program does
print(' ')
try:
    number = int(input('Eter an integer: ')) # Ask the user to enter a integer
    if number % 2 == 0: # If the remainder of the divison between the entered number and 2 is 0
        print(f'The number {number} is even!') # This number is even
    else: # Otherwise:
        print(f'The number {number} is odd!') # This number is odd
except ValueError: # If the user does not enter a integer:
    print(f'The number {number} is not a whole number, please enter a valid number.')