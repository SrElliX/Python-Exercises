# Exercise
# Ask the user to enter their name and age
# If name and age are entered:
# Display:
# Your name and {name}
# Your name reversed and {name reversed}
# Whether name contains spaces or not
# Your name contains {n} letters
# The first letter of your name is {letter}
# The last letter of your name is {letter}
# If nothing is entered in name or age:
# Display: "Sorry, you left fields empty."

name = input('Enter your name: ')
age = input('Now your age: ')

if name and age:
    print(f'Your name is {name}')
    print(f'Your reversed name is {name[::-1]}')
    
    if ' ' in name:
        print('Your name contains spaces.')
    else:
        print('Your name does not contains spaces.')
    
    print(f'Your name contains {len(name)} latters')
    print(f'The first latter of your name is {name[0]}')
    print(f'The last latter of your name is {name[-1]}')
else:
    print('Sorry, you left fields empty.')