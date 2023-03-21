#enter_pin.py

#Enters a previously decided pin through a loop until the right answer is given

print('BANK OF MUSPIRED')

pin = int(input('Enter your PIN: '))

while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))

    if pin == 1234:
        print('PIN accepted!')