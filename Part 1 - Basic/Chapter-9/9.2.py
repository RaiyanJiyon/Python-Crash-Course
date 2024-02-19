'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance
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

# Creating three instances of the Restaurant class
restaurant1 = Restaurant("The Great Feast", "Italian")
restaurant2 = Restaurant("Taco Haven", "Mexican")
restaurant3 = Restaurant("Sushi Palace", "Japanese")

# Calling describe_restaurant() for each instance
print("Restaurant 1:")
restaurant1.describe_restaurant()

print("\nRestaurant 2:")
restaurant2.describe_restaurant()

print("\nRestaurant 3:")
restaurant3.describe_restaurant()
