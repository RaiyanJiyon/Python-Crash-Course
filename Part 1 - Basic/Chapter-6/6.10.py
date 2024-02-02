# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

# Existing data from 6.2
favorite_numbers = {
    "Akash": [10, 20],
    "Sabbir": [55, 65],
    "Tamim": [69, 79],
    "Ishaq": [82, 92],
    "Sohel": [1, 2]
}

# Loop through the dictionary and print each person’s name along with their favorite numbers
for person, numbers in favorite_numbers.items():
    # Use a list comprehension to convert numbers to strings
    numbers_str = ', '.join([str(num) for num in numbers])

    # Print the result
    print(f"{person}'s favorite numbers are: {numbers_str}")

    # Add an extra line for better readability between individuals
    print()
