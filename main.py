from lists import *
from myfunctions import *
# imports the list file to be used
# imports the functions file to be used

print("Welcome to waikato air booking services")

linebreak()
# is line break repeated multiple times

name = name()
# asks for users name and saves as name

choice = destination_calculate(destinations, 'destination', name, 
'Is this the correct destination', confirmation)
# used to print out the destinations
# this is for choosing a destination from the list
# prints the price and destination of the flight
# calls the confirmer to ask if correct destination returns choice

calculate(destination, choice)
