#Quadratic Formula Equation

a = int(input('Enter the \'a\' value: '))
b = int(input('Enter the \'b\' value: '))
c = int(input('Enter the \'c\' value: '))

root1 = (-b + (b**2 - (4 * a * c))**0.5)/ (2 * a)
root2 = (-b - (b**2 - (4 * a * c))**0.5)/ (2 * a)

print(root1)
print(root2)