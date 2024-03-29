# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# From 7.8
sandwich_orders = ["Classic Turkey Club",
                   "Veggie Delight Wrap",
                   "pastrami",
                   "Spicy Chicken BLT",
                   "pastrami",
                   "Caprese Panini",
                   "pastrami",
                   "Smoked Salmon Bagel with Cream Cheese"]

print("deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwich = []

for sandwich_order in sandwich_orders:
    print(f"I will make your {sandwich_order} Sandwich.")
    finished_sandwich.append(sandwich_order)

print("\nList for finished sandwich - ")

for finished in finished_sandwich:
    print(finished)

