import lists
import functions
# imports the list file to be used
# imports all the functions file to be used

print("Welcome to waikato air booking services")

functions.linebreak()
# is line break repeated multiple times

name = functions.name()
# asks for users name and saves as name
functions.linebreak()

print("{}, please choose a destination (Using numbers)"
.format(name.capitalize()))
# used to help the user understand what to do
print()

functions.list(lists.destinations, 'destination')
# used to print out the destinations

choice = functions.destination(lists.destinations)
# this is for choosing a destination from the list

functions.linebreak()

print('''Your choice is: {}
The price for this is: ${:.2f}
'''.format(lists.destinations[choice]['destination'],
           lists.destinations[choice]['price']))
# prints the price and destination of the flight

input('is this right?\n1: Yes \n2: No\nAnswer here: ')