# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

# •	 If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# •	 If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# •	 Write one version of this program that runs the if block and another that runs the else block.

#================================================================================================
# starts from 5.3 
#================================================================================================

# Version 1: Runs the if block (green alien)
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points")
else:
    print("The player just earned 10 points")

# Version 2: Runs the else block (yellow alien)
alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points")
else:
    print("The player just earned 10 points")