#dice_rolling_simulator.py

#Project 2 of 50. This simulates a dice roll. Since I'm a nerd I've included variation on the type of dice to roll.
#I have also included options to roll the dice multiple times and display the results.
import random

def Roll_Dice(sides, roll):
    results = []

    for i in range(roll):
        results.append(random.randint(1, sides))

    return results

def Print_Roll_Results(resultList):
    for i in range(len(resultList)):
        print(f'| Result #{i}: {resultList[i]}                                       |')
response = True

while(response):
    print('|---------------Dice Rolling Simulator---------------|')
    print('|                                                    |')
    print('| How many sides are on your die (1 - 100)?          |')
    sides_of_die = int(input())
    print('| How many times would you like to roll your die?    |')
    roll_attempts = int(input())
    results = Roll_Dice(sides_of_die, roll_attempts)
    print('|----------------Calculating Results-----------------|')
    Print_Roll_Results(results)
    print('| Would you like to perform this action again(Y/N)?  |')
    response = input().upper().strip() == 'Y'

print('Thank You for using my Dice Rolling Simulator! Hope to see you again!')