import lists
# imports the list file to be used
import functions
# imports all the functions file to be used

print("Welcome to waikato air booking services")

functions.linebreak()
# is line break

name = input("What would you like to be called? ").strip().lower()
# asks for users name and saves as name
functions.linebreak()

for x in lists.destinations[]:
    print x