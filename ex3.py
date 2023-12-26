# Python exercise

# Make a program that asks the user the time and, based on the time described, displays the appropriate greeting. EX: Good morning 0-11, Good afternoon 12-17 and good evening 18-23

print('GREETING - TIME')
print(' ')

time = input('Enter a time (0-23): ')

try:
    time = int(time) 
    if not 0 <= time <= 23:
        raise ValueError
except ValueError:
    print('Please, enter a valid time.')
    exit()
    
if 0 <= time <= 11:
    greeting = 'Good Morning!'
elif 12 <= time <= 17:
    greeting = 'Good Afternoon!'
else:
    greeting = 'Goodnight!'
    
print(f'{greeting}')

