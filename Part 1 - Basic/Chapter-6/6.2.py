# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    "Akash": 10,
    "Sabbir": 55,
    "Tamim": 69,
    "Ishaq": 82,
    "Sohel": 1
}

# Convert the set to a list
people_names = ["Akash", "Sabbir", "Tamim", "Ishaq", "Sohel"]

print(people_names[0], "'s favorite number is", favorite_numbers["Akash"])
print(people_names[1], "'s favorite number is", favorite_numbers["Sabbir"])
print(people_names[2], "'s favorite number is", favorite_numbers["Tamim"])
print(people_names[3], "'s favorite number is", favorite_numbers["Ishaq"])
print(people_names[4], "'s favorite number is", favorite_numbers["Sohel"])
