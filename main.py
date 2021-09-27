import lists
import functions
# imports the list file to be used
# imports all the functions file to be used

print("Welcome to waikato air booking services")

functions.linebreak()
# is line break repeated multiple times

name = input("What would you like to be called? ").strip().lower()
# asks for users name and saves as name
functions.linebreak()

print("{} please choose a destination (Using numbers)".format(name.capitalize()))
# used to help user understand what to do
print()

y = 0
for x in lists.destinations:
    y += 1
    print("{}: {}".format(y, x))
# used to print out the destinations
while True:
    choice = input("Answer here: ")
    if choice in lists.prices:
        break
    else:
        print("That is not a destination")