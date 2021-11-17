import random

def name():
    fname = input('Please input your First Name here: ').lower()
    lname = input('Please input you Last Name here: ').lower()
    name = fname.capitalize() + " " + lname.capitalize()
    return name


# customizable line break
# length max recomend 93
def linebreak(shape='-', length=80, gap=1, line=''):
    while gap != 0:
        print('')
        gap -= 1
    while length != 0:
        line += shape
        length -= 1
    print(line)


# main function that the program loops back to
def menu(dicti, destinations, users, dates):
    while True:
        print('Hello welcome to waikato air booking service')
        linebreak()
        while True:
            print('Please pick an option using numbers\n')
            for x in dicti.keys():
                print('{}: {}'.format(x, dicti[x]))
            choice = input('Enter here: ')
# is the menu choices
            if choice == '1':
                linebreak()
                name_string = name()
                linebreak()
                choice, price = choice_desti(destinations)
                choice_date = date(dates)
                if choice_date == '1':
                    print('due to your')
                    price = discounter(destinations, choice)
                destination = 'Waikato to ' + choice
                users[name_string] = destination
                break
            elif choice == '2':
                linebreak()
                user_display(users)
                linebreak()
            elif choice == '3':
                linebreak()
                print('Thank you for booking with waikato air servcies')
                break
            else:
                print("\nI'm sorry that is not an option")
                linebreak()
        if choice == '3':
            break


# is a simple destination chooser with a confirmation
def choice_desti(destinations):
    while True:
        print('Please choose a destination')
        for x in destinations.keys():
            for y in destinations[x].keys():
                print('{}: Waikato to {} ${}'.format(x, y, destinations[x][y]))
        while True:
            choice_destination = input('enter here: ')
            linebreak()
            if choice_destination in destinations:
                for p in destinations[choice_destination].keys():
                    pass
# line above fixes an error
                print('Your choice is: Waikato to {}'.format(p))
# loop exist in case one enters an answer that is not included
                while True:
                    print('Is this right?\n1: Yes\n2: No')
                    choice = input('Enter here: ')
                    if choice == '1':
                        break
                    elif choice == '2':
                        break
                    else:
                        print('That is not a choice')
                linebreak()
                break
            else:
                print('That is not a choice')
        if choice == '1':
            price = destinations[choice_destination][p]
            break
    return choice_destination, price


def date(current_date):
    while True:
        print('When will you be flying?')
        for x in current_date:
            print(x)
        choice = input('Enter here: ')
        if choice == '1':
            break
        elif choice == '2':
            break
        else:
            print('That is not an option')
            linebreak()
    linebreak()
    return choice


def discounter(destinations, choice):
    for x in destinations[choice]:
        pass
    p = destinations[choice][x]
    print(p)
    pass
    discount_per = random.randrange(5,11)
    discount = discount_per / 100
    discounted_price = p - p * discount
# the math used for the discount
    print('Your discount is {}%\nYour flight price is now ${}'.format(discount_per, discounted_price))
    linebreak()
    return discounted_price


# displays all the users that have booked on the device
def user_display(users):
    print('Name: Destination')
    for x in users.keys():
        print('{}: {}'.format(x, users[x]))
