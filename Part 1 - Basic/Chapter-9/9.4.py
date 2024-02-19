'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business
'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        # Initialize attributes for restaurant name, cuisine type, and number served
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        # Method to print the restaurant's name and cuisine type
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

    def open_restaurant(self):
        # Method to print a message indicating that the restaurant is open
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number):
        # Method to set the number of customers served
        self.number_served = number

    def increment_number_served(self, increment):
        # Method to increment the number of customers served
        self.number_served += increment

# Creating an instance of the Restaurant class
restaurant = Restaurant("The Great Feast", "Italian")

# Printing individual attributes
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Changing the number of customers served and printing the updated value
restaurant.number_served = 50
print("\nNumber of Customers Served:", restaurant.number_served)

# Using set_number_served() method to set a new number of customers served
restaurant.set_number_served(100)
print("Number of Customers Served:", restaurant.number_served)

# Using increment_number_served() method to increment the number of customers served
restaurant.increment_number_served(50)
print("Number of Customers Served:", restaurant.number_served)
