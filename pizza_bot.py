# pizza bot program
import random
from random import randint

#List of names
names = ["Naomi", "Mio", "Rosmarie", "Kyle", "Dominicus", "Reigo", "Sheryl", "Lykke", "Hamid", "Sean"]

# Welcome message with random name
def welcome():

    '''
    Purpose: to generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
   

    num = randint(0,9)

    name = (names[num])

    print('*** Welcome to Dream Pizza ***')
    print('*** My name is ',name, '***')
    print("*** I will help you order your delicious dream pizza ***")



# Menu for pickup or delivery 




# Pick up information: name and phone




# Delivery information: name, address and phone





# Choose total number of Pizzas (max 5)




# Pizza menu




# Pizza ordering function - from menu (print each pizza ordered with cost)




# Print the order out - including if the order is pickup or delivery and the names and price of each pizza
# total cost including any delivery charge




# Ability to cancel or proceed with order




# Option for a new order or to exit




# Main function