# Fuction used to make linebreaks
def linebreak():
    print('''
--------------------------------------------''')

# Function for listing of items from a dictonarie
# Can only be used to call nested dictonaries 
def list(dict, sub_list):
    y = 1
    for x in dict:
        print("{}: {}".format(y, dict[x][sub_list]))
        y += 1 

# Just an maximuinm charter limit for names
def name():
    while True:
        name = input('''What would you like to be called? (min 3, max 28)
        Enter Here: ''').strip('!').lower()
        if len(name) <= 28 and len(name) >= 3:
            break
        elif len(name) >= 28 or len(name) <= 3:
            print('That name is to long or short')
        else:
            print("I don't know how you did this")
    return name