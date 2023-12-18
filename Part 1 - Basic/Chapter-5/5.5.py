# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed for the appropriate color alien


#================================================================================================
# starts from 5.4 
#================================================================================================

# Version 1: Green alien (5 points)
alien_color = 'green'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

# Version 2: Yellow alien (10 points)
alien_color = 'yellow'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

# Version 3: Red alien (15 points)
alien_color = 'red'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")