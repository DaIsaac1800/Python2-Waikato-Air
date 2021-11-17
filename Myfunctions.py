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
def menu(dicti, destinations, users):
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
                choice = choice_desti(destinations)
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


# is a simple destination chooser
def choice_desti(destinations):
    while True:
        print('Please choose destination')
        for x in destinations.keys():
            for y in destinations[x].keys():
                print('{}: Waikato to {} ${}'.format(x, y, destinations[x][y]))
        while True:
            choice_destination = input('enter here: ')
            linebreak()
            if choice_destination in destinations:
                for p in destinations[choice_destination].keys():
                    pass
                print('Your choice is: Waikato to {}'.format(p))
                while True:
                    print('Is this right?\n1: Yes\n2: No')
                    choice = input('Enter here: ')
                    if choice == '1':
                        break
                    elif choice == '2':
                        break
                    else:
                        print('That is no choice')
                linebreak()
                break
        if choice == '1':
            break
    for x in destinations[choice_destination]:
        choice_destination = x
    return choice_destination


# displays all the users that have booked
def user_display(users):
    print('Name: Destination')
    for x in users.keys():
        print('{}: {}'.format(x, users[x]))
