""" 8-9. Magicians: Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list. """

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
