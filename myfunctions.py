import random
# adds the random function to be used to add discounts

# fuction used to make linebreaks
def linebreak():
    print('''
======================================================================''')


# destination chooser
# function for listing off avaliable destinations
# allowing the user to choose from a nested dictonarie
def destination(dicti, sub_list, name):
    print("{}, please choose a destination (Using numbers)\n"
          .format(name.capitalize()))
    y = 1
    for x in dicti:
        print("{}: {}".format(y, dicti[x][sub_list]))
        y += 1
    while True:
        choice = input("Answer here: ")
        if choice in dicti:
            break
        else:
            print('That is not a choice')
    linebreak()
# returns the choosen answer provided by user
    return choice


# maximuinm chacter limit for names and asking for names
def name():
    while True:
        name = input('''What would you like to be called? (min 2, max 26)
Enter Here: ''').strip().lower()
        if len(name) <= 26 and len(name) >= 2:
            break
        elif len(name) >= 26 or len(name) <= 2:
            print('That name is not valid')
        else:
            print("I don't know how you did this")
    linebreak()
    return name


# calculates a discount using the random module and math
def calculate(dicti, choice):
    x = random.randrange(0, 290)
    y = x / 100
    discount = 100 - y
    discount_price = dicti[choice]['price'] - dicti[choice]['price'] * discount
    print('''You have been alloated a discount of {}%
Your price now is: ${:.2f}'''.format(discount, discount_price))


# prints the price and destination of the flight
def price(dicti, choice):
    print('''Your choice is: {}
The price for this is: ${:.2f}
    '''.format(dicti[choice]['destination'],
               dicti[choice]['price']))


# a repetable confirmer if there is two answers
def confirmer(question, list):
    while True:
        confirm = input('{}\n1: Yes \n2: No\nAnswer here: '
                        .format(question)).lower()
        if confirm in list[0]:
            return confirm
            break
        elif confirm in list[1]:
            return confirm
            break
        else:
            print('that is not a choice avalible')


# a combination of destination and price
def destination_calculate(dicti, sub_list, name, question, list):
    print("{}, please choose a destination (Using numbers)\n"
          .format(name.capitalize()))
    y = 1
    for x in dicti:
        print("{}: {}".format(y, dicti[x][sub_list]))
        y += 1
    while True:
        choice = input("Answer here: ")
        if choice in dicti:
            break
        else:
            print('That is not a choice')
    linebreak()
    print('''Your choice is: {}
The price for this is: ${:.2f}
          '''.format(dicti[choice]['destination'],
          dicti[choice]['price']))
    while True:
        confirm = input('{}\n1: Yes \n2: No\nAnswer here: '
                        .format(question)).lower()
        if confirm in list[0]:
            linebreak()
            break
        elif confirm in list[1]:
            linebreak()
            destination_calculate(dicti, sub_list, name, question, list)
        else:
            print('that is not a choice avalible')
    return choice
