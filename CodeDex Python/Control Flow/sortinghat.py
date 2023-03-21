#sortinghat.py
#Ask user questions and print out the house with the most points

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    1) Dusk')

q1Input = int(input('Enter value of answer: '))

if q1Input == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1Input == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print('\nQ2) When I\'m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')

q2Input = int(input('Enter value of answer: '))

if q2Input == 1:
    hufflepuff += 1
elif q2Input == 2:
    slytherin += 1
elif q2Input == 3:
    ravenclaw += 1
elif q2Input == 4:
    gryffindor += 1
else:
    print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('\nQ3) Which kind of instrument most pleases your ear?')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

q3Input = int(input('Enter value of answer: '))

if q3Input == 1:
    slytherin += 1
elif q3Input == 2:
    hufflepuff += 1
elif q3Input == 3:
    ravenclaw += 1
elif q3Input == 4:
    gryffindor += 1
else:
    print('Wrong input.')

if gryffindor >= slytherin and gryffindor >= ravenclaw and gryffindor >= hufflepuff:
    print('🦁 Gryffindor!')

elif ravenclaw >= slytherin and ravenclaw >= hufflepuff:
    print('🦅 Ravenclaw!')

elif hufflepuff >= slytherin:
    print('🦡 Hufflepuff!')

else:
    print('🐍 Slytherin!')