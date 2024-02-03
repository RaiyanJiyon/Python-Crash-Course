""" 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name. """


# From 8.10
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
