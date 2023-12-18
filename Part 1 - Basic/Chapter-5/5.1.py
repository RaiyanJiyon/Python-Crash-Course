# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
''' car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi') '''
# •	 Look closely at your results, and make sure you understand why each line 
# evaluates to True or False.
# •	 Create at least 10 tests. Have at least 5 tests evaluate to True and another 
# 5 tests evaluate to False


# Conditional Tests
number = 7
text = "Hello"
floating_number = 3.14

# Test 1: Equality check
print("Test 1: Is number equal to 7? I predict True.")
print(number == 7)

# Test 2: Inequality check
print("\nTest 2: Is text not equal to 'World'? I predict True.")
print(text != 'World')

# Test 3: Greater than check
print("\nTest 3: Is number greater than 5? I predict True.")
print(number > 5)

# Test 4: Less than or equal to check
print("\nTest 4: Is floating_number less than or equal to 3.14? I predict True.")
print(floating_number <= 3.14)

# Test 5: Logical AND
print("\nTest 5: Is number greater than 5 and text starts with 'H'? I predict True.")
print(number > 5 and text.startswith('H'))

# Test 6: Logical OR
print("\nTest 6: Is number less than 5 or floating_number equal to 3.14? I predict False.")
print(number < 5 or floating_number == 3.14)

# Test 7: Membership test (in)
print("\nTest 7: Is 'lo' in text? I predict True.")
print('lo' in text)

# Test 8: Membership test (not in)
print("\nTest 8: Is 'xyz' not in text? I predict True.")
print('xyz' not in text)

# Test 9: Check if a string is empty
empty_string = ""
print("\nTest 9: Is empty_string empty? I predict True.")
print(not empty_string)

# Test 10: Check if a list is not empty
non_empty_list = [1, 2, 3]
print("\nTest 10: Is non_empty_list not empty? I predict True.")
print(bool(non_empty_list))
