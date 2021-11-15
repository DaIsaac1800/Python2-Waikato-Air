def name():
    fname = input('Please Name here: ')
    return fname

# length max recomend 93
def linebreak( shape = '-', length = 80, gap = 1, line = ''):
    while gap != 0:
        print('')
        gap -= 1
    while length != 0:
        line += shape
        length -= 1
    print(line)


def menu(dicti, destinations, users):
    while True:
        fname = name()
        linebreak()
        print('Hello {} welcome to waikato air booking service'.format(fname))
        linebreak()
        while True:
            print('Please pick an option using numbers\n')
            for x in dicti.keys():
                print('{}: {}'.format(x, dicti[x]))
            choice = input('Enter here:')
            if choice == '1':
                linebreak()
                choice = choice_desti(destinations)
                destination = 'Waikato to ' + choice
                users[fname] = destination
                break
            elif choice == '2':
                linebreak()
                user_display(users)
            elif choice == '3':
                print('\nThank you for booking')
                break
            else:
                print('no')
                linebreak()
        if choice == '3':
            break


def choice_desti(destinations):
    while True:
        print('Please choose destination')
        for x in destinations.keys():
            for y in destinations[x].keys():
                print('{}: Waikato to {} {}'.format(x, y ,destinations[x][y]))
        while True:
            choice_destination = input('enter here: ')
            linebreak()
            if choice_destination in destinations:
                print('Your choice is: Waikato to {}'.format(y))
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


def user_display(users):
    print('Name: Destination')
    for x in users.keys():
        print('{}: {}'.format(x, users[x]))
    

