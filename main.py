import lists
import functions
# imports the list file to be used
# imports all the functions file to be used

print("Welcome to waikato air booking services")

functions.linebreak()
# is line break repeated multiple times

name = functions.name()
# asks for users name and saves as name

choice = functions.destination(lists.destinations, 'destination', name)
# used to print out the destinations
# this is for choosing a destination from the list
# used to help the user understand what to do

functions.price(lists.destinations, choice)
# prints the price and destination of the flight

confirm = functions.confirmer('Is this the correct destination',
                              lists.confirmation)
# calls the confirmer to ask if correct destination and returns it
