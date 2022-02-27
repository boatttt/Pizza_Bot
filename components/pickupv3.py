customer_details = {}


print('Please enter the pickup information')
valid = False
while not valid:
#Customer name
    customer_details['name'] = input('What is your name? ')
    if customer_details['name'] != '':
        print(customer_details['name'])
        break

    else:
        print('Sorry, this cannot be left blank')


valid = False
while not valid:
#Phone number
    customer_details['phone'] = input('Please enter your phone number ')
    if customer_details['phone'] != '':
        print(customer_details['phone'])
        break

    else: 
        print('Sorry, this cannot be left blank')