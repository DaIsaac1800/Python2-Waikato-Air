def name():
    fname = input('Please Name here:')
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


def menu(dicti):
    fname = name()
    print('Hello {} welcome to waikato air booking service'.format(fname))
    linebreak()
    print('Please pick an option using numbers\n')
    for x in dicti.keys():
        print('{}: {}'.format(x, dicti[x]))
    while True:
        choice = input('Enter here:')
        if choice == '1':
            print(choice)
            break
        elif choice == '2':
            print(choice)
            break
        elif choice == '3':
            print(choice)
            break
        else:
            print('no')

def destinations():
    print('Please choose destination')
