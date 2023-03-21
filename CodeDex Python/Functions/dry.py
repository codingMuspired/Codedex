#dry.py

#Looking through previously used functions

genericList = ['pizza', 'car', 'video game']
genericNum = [1, 2 ,3 ,4 ,5]


#len() returns the length of the object in this case the length of my genericList
print(f'Generic List Length Using len():      {len(genericList)}')

#max() returns the max value in the object given in this case my genericNum list
print(f'Max number in genericNum using max(): {max(genericNum)}')

#min() returns the minimum value in the object given in this case my genericNum list
print(f'Min number in genericNum using min(): {min(genericNum)}')

#print() prints the object to the stream
print("This is a statement output with the print function")

#range() helps us to go through a loop based on either a stop or start,stop,step combo
for item in range(len(genericList)):
    print(f'{genericList[item]} is printed through a loop using range')