# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the change.
# •	 The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# Original menu
restaurant_foods = ("Burger", "Pizza", "Pasta", "Salad", "Steak")

# Print each food the restaurant offers
print("Original Menu:")
for restaurant_food in restaurant_foods:
    print(restaurant_food)

# Try to modify one of the items (this will result in an error)
# Uncomment the line below to see the error
# restaurant_foods[2] = "Soup"

# The restaurant changes its menu, replacing two items
new_menu = ("Fish", "Chicken", "Pasta", "Salad", "Vegetables")

# Print each item on the revised menu
print("\nRevised Menu:")
for new_item in new_menu:
    print(new_item)
