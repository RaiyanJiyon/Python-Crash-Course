# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

pizza = []

while True:
    topping = input("Enter a series of pizza toppings. Or, enter 'quit' to exit: ")

    if topping.lower() == 'quit':
        break

    pizza.append(topping)
    print(f"You’ll add the {topping} topping to their pizza.")

# Print the final list of pizza toppings
print("Your pizza toppings are:", ', '.join(pizza))
