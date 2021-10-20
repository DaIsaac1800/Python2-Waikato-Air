# fuction used to make linebreaks
def linebreak():
    print('''
--------------------------------------------''')

# function for listing off items from a dictonarie
# can only be used to call double nested dictonaries 
def list(dict, sub_list):
    y = 1
    for x in dict:
        print("{}: {}".format(y, dict[x][sub_list]))
        y += 1 

# maximuinm chacter limit for names and asking for names
def name():
    while True:
        name = input('''What would you like to be called? (min 2, max 26)
Enter Here: ''').strip('!').lower()
        if len(name) <= 26 and len(name) >= 2:
            break
        elif len(name) >= 26 or len(name) <= 2:
            print('That name is incorrect')
        else:
            print("I don't know how you did this")
    return name

# destination chooser
def destination(dict):
    while True:
        choice = input("Answer here: ")
        if choice in dict:
            break
        else:
            print('That is not a choice')
    return choice
