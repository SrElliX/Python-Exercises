# Make a shopping list with lists
# The user must be able to insert, delete and list values from their list
# Do not allow the program to break with errors due to non-existent indexes in the list

import os

shopp_list = []
while True:
    print('Choose an option')
    option = input('[i]nsert [d]elet [l]ist [s]ave: ')
    
    if option == 'i':
        os.system('cls')
        value = input('Value: ')
        shopp_list.append(value)
        continue
    elif option == 'd':
        index_str = input('Choose the index of the value to be deleted: ')
        
        try:
            index = int(index_str)
            del shopp_list[index]
            continue
        except ValueError:
            print('Enter an existing index in the list.')
        except IndexError:
            print('Enter an existing index in the list.')
        except Exception:
            print('Error :/')
            continue
    elif option == 'l':
        os.system('cls')
        
        if len(shopp_list) == 0:
            print('There are no objects in the list.')
            
        for i, value in enumerate(shopp_list):
            print(i, value)
        continue
    elif option == 's':
        os.system('cls')
        def save_list(list, file_name):
            with open(file_name, 'w') as file:
                for item in list:
                    file.write(f'{item}\n')
        the_file_name = input('What name do you want to give your list? ')
        save_list(shopp_list, the_file_name)
    
        print(f'The list has been saved to the file: {the_file_name}')
    else:
        print('Enter a valid option (i, d, l, s)')