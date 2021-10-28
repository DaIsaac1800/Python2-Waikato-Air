import Lists
def confirm(list):
    while True:
        confirm = input('Yes or No').lower()
        if confirm not in list[0] and confirm not in list[1]:
            print('Invalid answer')
        else:
            break
    return confirm
print(confirm(Lists.confirm))