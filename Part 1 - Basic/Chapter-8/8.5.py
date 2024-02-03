""" 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country. """

# Define a function called describe_city
def describe_city(city, country="Bangladesh"):
    # Print a simple sentence describing the city and its country
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Dhaka")  # Uses the default country value ("Bangladesh")
describe_city("Sylhet")  # Uses the default country value ("Bangladesh")
describe_city("Reykjavik", "Iceland")  # Provides a custom country value ("Iceland")
