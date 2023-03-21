#favorite_cities.py

#The program demonstrates how to use __init__() with classes

class City:
    def __init__(self, name, country, population, landmarks, nicknames):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.nicknames = nicknames

nyc = City('New York City', 'United States of America', '8.468 million', ['Statue of Liberty', 'Empire State Building', 'Central Park'], 'The Big Apple')
ana = City('Anaheim', 'United States of America', '345,940', ['Disneyland', 'Angel Stadium', 'Honda Center'], 'House of Mouse')

print(vars(nyc))
print(vars(ana))