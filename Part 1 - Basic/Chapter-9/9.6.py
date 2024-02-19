'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method.
'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize attributes for restaurant name and cuisine type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        # Method to print the restaurant's name and cuisine type
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        # Method to print a message indicating that the restaurant is open
        print(f"The restaurant {self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        # Initialize attributes for ice cream stand including flavors
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        # Method to display available ice cream flavors
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(flavor)

# Creating an instance of IceCreamStand and calling the method to display flavors
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
