#rocket.py

#Scenario where we needs to convert a kilometer distance to miles to help out nasa
#More fun with functions

def distance_to_miles(distance):
    return distance / 1.609

answer = distance_to_miles(int(input('Please enter the value to be converted: ')))
print(answer)