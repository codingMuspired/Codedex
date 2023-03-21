#grades.py
import random

grade = random.randint(0,100)

print(grade)

if grade > 60:
    print("You passed.")
else:
    print("You failed.")