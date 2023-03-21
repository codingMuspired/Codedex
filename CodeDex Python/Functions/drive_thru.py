#drive_thru.py

# Create a drive thru function that takes a users order

def welcome():
    print('Welcome to Muspired\'s Munchie Minute')
    print('Please select an item from the menu:')
    print('1.  🍔 Cheeseburger')
    print('2.  🍔🍔 Double Cheeseburger')
    print('3.  🥓🍔 Bacon Cheeseburger')
    print('4.  🥪 BLT Sandwich')
    print('5.  🌭 Hot Dog')
    print('6.  🍟 Fries')
    print('7.  🥤 Soda')
    print('8.  🍺 Beer')

def get_menuItem(x):
    if x == 1:
        return '🍔 Cheeseburger'
    elif x == 2:
        return '🍔🍔 Double Cheeseburger'
    elif x == 3:
        return '🥓🍔 Bacon Cheeseburger'
    elif x == 4:
        return '🥪 BLT Sandwich'
    elif x == 5:
        return '🌭 Hot Dog'
    elif x == 6:
        return '🍟 Fries'
    elif x == 7:
        return '🥤 Soda'
    elif x == 8:
        return '🍺 Beer'
    else:
        return "invalid option"

welcome()

choice = int(input('What would you like to order? '))
print(get_menuItem(choice))