def linebreak():
    print('''
--------------------------------------------''')

def list(dict, sub_list):
    y = 1
    for x in dict:
        print("{}: {}".format(y, dict[x][sub_list]))
        y += 1 
