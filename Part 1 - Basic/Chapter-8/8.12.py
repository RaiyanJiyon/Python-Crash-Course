""" 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time. """

def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Sandwich is ready!\n")

# Call the function three times with a different number of arguments each time
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss")
make_sandwich("Tuna")
