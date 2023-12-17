# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

# •	 Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

# •	 Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.

# •	 Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.


# 4-10. Slices
animals = ["Cheetah", "Lion", "Leopard", "Cat", "Dog", "Gorilla", "King-Kong"]

# Print the first three items in the list
print("The first three items in the list are:", animals[:3])

# Print three items from the middle of the list
print("Three items from the middle of the list are:", animals[2:5])

# Print the last three items in the list
print("The last three items in the list are:", animals[-3:])
