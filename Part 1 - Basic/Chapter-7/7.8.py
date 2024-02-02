# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


sandwich_orders = ["Classic Turkey Club",
                   "Veggie Delight Wrap",
                   "Spicy Chicken BLT",
                   "Caprese Panini",
                   "Smoked Salmon Bagel with Cream Cheese"]

finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

print("\nList of finished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")

