import datetime
# imports the date time module so it can be used in a list

menu_choices = {'1': 'Choose destination', '2': 'View users booked', '3': 'Exit'}

destinations = {'1': {'Wellington': 189},
                '2': {'Chirstchurch': 189},
                '3': {'Queenstown': 189}}

users = {}

dates = ('Current date: {}'.format(datetime.datetime.now().strftime('%x')),
         '1: Tommorow', '2: Next Week')