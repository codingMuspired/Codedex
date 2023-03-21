#pokedex.py

# Simulate a pokedex entry using what we have learned from classes

class Pokemon:
    def __init__(self, entry, name, type, description, is_caught, level, region, height, weight):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught
        self.level = level
        self.region = region
        self.height = height
        self.weight = weight

    def speak(self):
        print(self.name + ' made a sound!')

    def display_details(self):
        print('Entry: #' + "{:04d}".format(self.entry))
        print('Name: ' + self.name)
        print(f'Height: {self.height}m')
        print(f'Weight: {self.weight}kg')
        if len(self.type) == 1:
            print('Type: ' + self.type[0])
        else:
            print('Type: ' + self.type[0] + '/' + self.type[1])

        print(f'Lv. {self.level}')
        print('Region: ' + self.region)
        print('Description: ' + self.description)

        if self.is_caught:
            print(self.name + ' has already been caught!')
        else:
            print(self.name + ' hasn\'t been caught yet.')

flareon = Pokemon(136, 'Flareon', ['Fire'], 'Flareon evolves from Eevee using a Fire Stone. It has an internal fire sac that lets its fire rise up to 1,600 degrees F.', True, 62, 'Kanto', 0.9, 25)

flareon.speak()

flareon.display_details()

tinkaton = Pokemon(959, 'Tinkaton', ['Fairy', 'Steel'], 'The hammer tops 220 pounds, yet it gets swung around easily by Tinkaton as it steals whatever it pleases and carries its plunder back home.', False, 40, 'Paldea', 0.7112, 112.809)

tinkaton.speak()

tinkaton.display_details()

gengar = Pokemon(94, 'Gengar', ['Ghost', 'Poison'], 'To steal the life of its target, it slips into the prey\'s shadow and silently waits for an opportunity.', True, 85, 'Kanto', 1.4986, 40.51)

gengar.speak()

gengar.display_details()