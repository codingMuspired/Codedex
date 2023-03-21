#my bmi via codedex
#Hope i can survive looking at this

massPounds = 245 #my weight in pounds :'(
massKG = massPounds * 0.45359237 #Converted pounds weight to kilo to use given equaton
heightInches = 70 #My height in inches. Easier to give without some weird decimals for feet
heightMeters = heightInches / 39.37 #Converting inches height to meters for equation
bmi = massKG / (heightMeters**2) #Calculate BMI

print(bmi) #Print out bmi and pray :'(