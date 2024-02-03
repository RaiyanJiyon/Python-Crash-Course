""" 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that’s returned. """

# Define a function called city_country
def city_country(city, country):
    # Return a formatted string containing the name of the city and its corresponding country
    return f"{city}, {country}"

# Call the function with three city-country pairs and print the returned values
place1 = city_country("Dhaka", "Bangladesh")
print(place1)

place2 = city_country("Delhi", "India")
print(place2)

place3 = city_country("London", "England")
print(place3)
