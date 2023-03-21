#ph_levels.py

# Ask for phlevel from user and return whether basic/acidic/neutral
# Testing Elif Statements

pH = int(input('Please enter a pH value between 0 and 14: '))

if pH > 7:
    print("Basic")

elif pH < 7:
    print('Acidic')

else:
    print('Neutral')