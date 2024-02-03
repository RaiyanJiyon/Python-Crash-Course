""" 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import * """

# Approach 1: Import the entire module
import my_module

# Approach 2: Import only the specific function
from my_module import greet

# Approach 3: Import with an alias
from my_module import greet as my_greet

# Approach 4: Import the entire module with an alias
import my_module as mm

# Approach 5: Import all functions from the module
from my_module import *

# Call the function using each approach
my_module.greet("Alice")  # Approach 1
greet("Bob")              # Approach 2
my_greet("Charlie")       # Approach 3
mm.greet("David")         # Approach 4
greet("Eve")              # Approach 5
