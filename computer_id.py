# computer_id.py
# Author: Aurelien, Feb 2021
# Shows information about the machine

import platform

# This function shows information about the OS
def os_information():
    print('Your OS is: ', platform.uname())

# Information about the processor
def proc_information():
    print('Your CPU is: ', platform.processor())

# Information about the Python version
def p_version():
    print('Your Python version is: ', platform.python_version())




# Main function: menu
def menu():
    options = '''Please choose from:
1 - Display information about the OS
2 - Display information about the CPU
3 - Display information about Python
4 - Quit'''

    userChoice = '' # Empty string

    # Main loop
    while userChoice != '4':
        # Display the options
        print(options)
        # Get the user's choice
        userChoice = input('What is your selection?')

        # Take appropriate actions based on input
        if userChoice == '1':
            os_information()
        elif userChoice == '2':
            proc_information()
        elif userChoice == '3':
            p_version()
        elif userChoice == '4':
            print('Goodbye')
        else:
            print('Invalid input')


# Point out the entry of the program
if __name__ == '__main__':
    menu()
