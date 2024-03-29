# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


# Modified make_shirt() function
def make_shirt(size="Large", message="I Love Python."):
    print(f"The size of the shirt - {size}\n{message}")

# Make a large shirt with the default message
make_shirt()

""" Make a medium shirt with the default message
make_shirt("Medium")

# Make a shirt of any size with a different message
make_shirt("Small", "Custom message for a small shirt.") """
