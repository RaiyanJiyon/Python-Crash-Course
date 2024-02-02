# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    "Dhaka": {
        "country": "Bangladesh",
        "population": "23,210,000",
        "fact": "World's no. 1 air pollution city."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "13,515,000",
        "fact": "Known for advanced technology."
    },
    "New York": {
        "country": "USA",
        "population": "8,398,748",
        "fact": "Cultural and financial hub."
    }
}

# Print information about each city
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()