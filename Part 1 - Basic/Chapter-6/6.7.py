# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

# Existing code from 6.1
person_details1 = {"first_name": "Abdur", "last_name": "Razzaq", "age": 24, "city": "Dhaka"}
person_details2 = {"first_name": "Rajib", "last_name": "Khan", "age": 25, "city": "Barishal"}
person_details3 = {"first_name": "Tamim", "last_name": "Iqbal", "age": 35, "city": "Chittagong"}

# Store all three dictionaries in a list called people
people = [person_details1, person_details2, person_details3]

# Loop through the list of people
for person in people:
    print("Person Details - ")

    # Iterate through the dictionary for each person and print key-value pairs
    for key, value in person.items():
        print(f"{key}: {value}")

    # Add an extra line for better readability between people
    print()
