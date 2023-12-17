# -2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

# •	 Modify your program to print a statement about each animal, such as A dog would make a great pet.

# •	 Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!

animals_with_common_characteristic = ["Cheetah", "Lion", "Leopard"]

# Print the name of each animal
print("Animals:")
for animal in animals_with_common_characteristic:
    print(animal)

# For extra space
print("\n")

# Print a statement about each animal
print("Animal Statements:")
for animal in animals_with_common_characteristic:
    print(animal, "is a powerful big cat.")

# For extra space
print("\n")

# Print a final statement about what these animals have in common
print("Any of these animals would make a great pet!")
