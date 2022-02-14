import random
from random import randint

def welcome():

    '''
    Purpose: to generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
    #List of names
    names = ["Naomi", "Mio", "Rosmarie", "Kyle", "Dominicus", "Reigo", "Sheryl", "Lykke", "Hamid", "Sean"]

    num = randint(0,9)

    name = (names[num])

    print('*** Welcome to Dream Pizza ***')
    print('*** My name is ',name, '***')
    print("*** I will help you order your delicious dream pizza ***")

def main():
    '''
    Purpose: to run all the functions
    Parameters: None
    Returns: None 
    '''
    welcome()


main()