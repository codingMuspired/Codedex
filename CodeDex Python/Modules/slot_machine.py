#slot_machine.py

#Introduction to modules using a slot machine program

import random

symbols = ['🍒','🍇', '🍉', '7️⃣'] 

while(True):
    results = random.choices(symbols, k = 3)

    print(f'{results[0]}  |  {results[1]}  |  {results [2]}')

    if(results[0] == symbols[3] and results[1] == symbols[3] and results[2] == symbols[3]):
        print('Jackpot! 💰')

    else:
        print('Thanks for playing!')

    response = input('Would you like to play again again(Y/N)?').upper().strip() == 'Y'

    if(not response):
        print('Thanks for playing the game!')
        break