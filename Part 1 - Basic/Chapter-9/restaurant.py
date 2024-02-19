# restaurant.py

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize attributes for the restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Restaurant Name: {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.name} is now open!")
