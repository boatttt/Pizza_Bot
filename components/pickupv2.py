#Bugs
#Accepts blank input 

print('Please enter the pickup information')
valid = False
while not valid:
#Customer name
    name = input('What is your name? ')
    if name != '':
        print(name)
        break

    else:
        print('Sorry, this cannot be left blank')


valid = False
while not valid:
#Phone number
    phone = input('Please enter your phone number ')
    if phone != '':
        print(phone)
        break

    else: 
        print('Sorry, this cannot be left blank')