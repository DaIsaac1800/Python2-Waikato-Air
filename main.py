from lists import *
from myfunctions import *
# imports the list file to be used
# imports the functions file to be used

while True:
# makes it so the program repeats
    print("Welcome to waikato air booking services")

    linebreak()
# is line break repeated multiple times

    name_string = name()
# asks for users name and saves as name

    choice = destination_calculate(destinations, 'destination',
                               name_string,
                               'Is this the correct destination?',
                               confirmation_list)
# used to print out the destinations
# this is for choosing a destination from the list
# prints the price and destination of the flight
# calls the confirmer to ask if correct destination returns choice

    confirm = confirmer('Are you flying tomorrow?',
                        confirmation_list)
    linebreak()
    if confirm in confirmation_list[0]:
        calculate(destinations, choice)
        linebreak()
# used to ask and calculate a discount avalaible to the user
    
    confirm = confirmer('Do you want to book agian?',
                        confirmation_list)
    linebreak()
    if confirm in confirmation_list[1]:
        break
# confirmer and If statement thats makes the while true loop continue

print('Thank you for booking with Waikato air')
