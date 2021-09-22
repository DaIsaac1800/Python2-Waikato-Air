import Lists
def menu(list):
    no = 0
    for i in list:
         print(i)
    for i in list:
        for j in list[no]:
            print(j)
        no += 1
menu(Lists.test)