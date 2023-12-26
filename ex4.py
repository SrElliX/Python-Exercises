# Make a game for the user to guess the secret word.
# You will propose any secret word and give the user the possibility
# enter just one letter.
# When the user types a letter, you will check if the letter typed is in the word
# secret.
# If the letter entered is in the secret word: display the letter
# If the letter entered is NOT in the secret word: display *.
# Count your user's attempts

import os 

secret_word = 'batman'
correct_letters = ''
attempts = 0
while True:
    typed_letter = input('Enter any letter: ')
    attempts += 1
    
    if len(typed_letter) > 1:
        print('Please enter just one letter.')
        continue
    
    if typed_letter in secret_word:
        correct_letters += typed_letter
        
    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'
    print('Formed word: ', formed_word)
    if formed_word == secret_word:
        os.system('cls')
        print('Congratulations! You won!')
        print('The secret word was:', secret_word)
        print('Attepents:', attempts)
        

        correct_letters = ''
        attempts = 0
        
        break