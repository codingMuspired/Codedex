#the_cyclone.py

#more if statement works by creating a new entry system for a roller coaster

height = int(input('Please enter your height in cm: '))
credits = int(input('Please enter total amount of credits: '))
with_taller_person = input('Are you with a taller person(y/n): ').lower()

if height >= 137 and credits >= 10:
    print('Enjoy the ride!')

elif height < 137:
    if height < 100 or not with_taller_person:
        print('You\'re not tall enough for this ride yet.')
    elif height >= 100 and with_taller_person:
        print('Enjoy the ride!')

elif credits < 10:
    print('You don\'t have enough credits to ride')

else:
    print('Invalid data.')