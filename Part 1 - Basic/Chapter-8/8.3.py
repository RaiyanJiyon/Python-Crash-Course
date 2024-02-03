""" 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments. """

# Define a function called make_shirt
def make_shirt(size, message):
    # Print a sentence summarizing the size of the shirt and the message printed on it
    print(f"The size of the shirt - {size}\n{message}")

# Call the function once using positional arguments to make a shirt
make_shirt("XL", "I Believe That.")

# You can also call the function a second time using keyword arguments
make_shirt(size="M", message="Python Lover")

