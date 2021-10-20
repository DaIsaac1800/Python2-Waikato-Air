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

functions.price(lists.destinations, choice)
# prints the price and destination of the flight

while True:
    confirm = input('is this right?\n1: Yes \n2: No\nAnswer here: ')
    if confirm in lists.confirmation[0]:
        break
    elif confirm in lists.confirmation[1]:
        break
    else:
        print('that is not a choice avalible')
