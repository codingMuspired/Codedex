#bobs_burgers.py

#Learning more about classes and creating instances

class Restaurant:
    name = ''
    type = ''
    rating = 0.0
    delivery = True

diner = Restaurant()
diner.name = 'Bob\'s Burgers'
diner.type = 'American Diner'
diner.rating = 4.7
diner.delivery = False

print(vars(diner))

diner2 = Restaurant()
diner2.name = 'KBop'
diner2.type = 'Korean Restaurant'
diner2.rating = 5.0
diner2.delivery = False

print(vars(diner2))

diner3 = Restaurant()
diner3.name = 'Chick-fil-a'
diner3.type = 'American Fast Food'
diner3.rating = 4.8
diner3.delivery = True

print(vars(diner3))