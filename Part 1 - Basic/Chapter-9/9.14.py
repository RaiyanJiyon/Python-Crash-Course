'''
9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default 
value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.count = 0

    def roll_die(self):
        while self.count < 10:
            print(randint(1, self.sides))
            self.count += 1
        self.count = 0  # Reset count for the next roll

# Create a 6-sided die and roll it 10 times
print("Rolling a 6-sided die 10 times:")
six_sided_die = Die()
six_sided_die.roll_die()

# Create a 10-sided die and roll it 10 times
print("\nRolling a 10-sided die 10 times:")
ten_sided_die = Die(sides=10)
ten_sided_die.roll_die()

# Create a 20-sided die and roll it 10 times
print("\nRolling a 20-sided die 10 times:")
twenty_sided_die = Die(sides=20)
twenty_sided_die.roll_die()
