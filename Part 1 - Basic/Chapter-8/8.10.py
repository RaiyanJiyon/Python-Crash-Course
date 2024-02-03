""" 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified. """

# List of magician’s names
magician_names = [
    "Merlin the Magnificent",
    "Enchanto the Illusionist",
    "Mystique Mirage",
    "Zephyr the Wizard",
    "Sorcerella Stardust"
]

# Define a function called show_magicians
def show_magicians(magicians):
    # Loop through the list of magicians and print each name
    for magician in magicians:
        print(magician)

# Call the function and pass the list of magician's names
show_magicians(magician_names)

def make_great(names):
    # Modify the list by adding "the Great" to each magician’s name
    for i in range(len(names)):
        names[i] = "the Great " + names[i]

# Call the make_great function to modify the list
make_great(magician_names)

# Call the show_magicians function to see that the list has actually been modified
show_magicians(magician_names)
