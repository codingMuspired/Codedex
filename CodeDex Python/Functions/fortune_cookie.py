#fortune_cookie.py

# Gives user random fortune cookies...helps us to understand functions
import random
def fortune():
    randomNum = random.randint(1, 9)

    if randomNum == 1:
        print('Don\'t pursue happiness - create it.')
    elif randomNum == 2:
        print('All things are difficult before they are easy.')
    elif randomNum == 3:
        print('The early bird gets the worm, but the second mouse gets the cheese.')
    elif randomNum == 4:
        print('If you eat something and nobody sees you eat it, it has no calories.')
    elif randomNum == 5:
        print('Someone in your life needs a letter from you.')
    elif randomNum == 6:
        print('Don\'t just think. Act!')
    elif randomNum == 7:
        print('Your heart will skip a beat')
    elif randomNum == 8:
        print('The fortune you search for is in another cookie.')
    else:
        print('Help! I\'m being held prisoner in a Chinese bakery!')

fortune()
fortune()
fortune()