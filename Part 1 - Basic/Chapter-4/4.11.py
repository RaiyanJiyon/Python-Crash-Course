# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.Then, do the following:

# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

# Original pizza list
pizza_types = ["Margherita", "Pepperoni", "Vegetarian"]

# Duplicate pizza list
friend_pizzas = ["Margherita", "Pepperoni", "Vegetarian"]

# Add a new pizza to the original list
pizza_types.append("Hawaiian")

# Add a different pizza to the list friend_pizzas
friend_pizzas.append("BBQ Chicken")

# Print My favorite pizzas are: and then use a for loop to print the first list
print("My favorite pizzas are:")
for pizza_type in pizza_types:
    print(pizza_type)

print("\n")

# Print My friend’s favorite pizzas are: and then use a for loop to print the second list
print("My friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
