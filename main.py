import lists
import functions
# imports the list file to be used
# imports all the functions file to be used

print("Welcome to waikato air booking services")

print(lists.destinations)

functions.linebreak()
# is line break repeated multiple times

name = input("What would you like to be called? ").strip().lower()
# asks for users name and saves as name
functions.linebreak()

print("{} please choose a destination (Using numbers)".format(name.capitalize()))
# used to help user understand what to do
print()

y = 1
for x in lists.destinations:
    print("{}: {}".format(y, lists.destinations[x]['destination']))
    y += 1
# used to print out the destinations
while True:
    choice = int(input("Answer here: "))
    if choice in lists.destinations:
        break
    else:
        print('That is not a choice')
# this is for choosing a destination from the list

print('''Your choice is: {}
The price for this is: ${}
'''.format(lists.destinations[choice]['destination'],
           lists.destinations[choice]['price']))