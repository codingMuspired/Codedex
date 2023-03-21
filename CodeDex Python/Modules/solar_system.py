#solar_system.py

#Using from and as with modules 

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if(random_planet == 'Mercury'):
    planet_radius = 2440

elif(random_planet == 'Venus'):
    planet_radius = 6052

elif(random_planet == 'Earth'):
    planet_radius = 6371

elif(random_planet == 'Mars'):
    planet_radius = 3390

elif(random_planet == 'Saturn'):
    planet_radius = 58232

else:
    print('Oops! An error occured.')

planet_area  = 4 * pi * (planet_radius ** 2)
print(f'Area of {random_planet}: {planet_area} km²')