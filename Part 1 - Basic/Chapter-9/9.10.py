'''
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
'''

# restaurant_import.py
from restaurant import Restaurant

# Create an instance of Restaurant
restaurant = Restaurant("Ristorante Italiano", "Italian")
# Call every method to show that the import statement is working properly
restaurant.describe_restaurant()
restaurant.open_restaurant()
