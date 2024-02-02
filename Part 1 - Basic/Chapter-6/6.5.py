# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.

major_rivers = {"nile": "egypt", "Ganga": "India", "Meghna": "Bangladesh"}

# Use a loop to print a sentence about each river
for river, country in major_rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")

# Use a loop to print the name of each river included in the dictionary.
print("\nRivers:")
for river in major_rivers:
    print(river.capitalize())

# Use a loop to print the name of each country included in the dictionary.
print("\nCountries:")
for country in major_rivers.values():
    print(country.capitalize())

