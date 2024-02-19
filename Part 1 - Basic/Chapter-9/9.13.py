'''
9-13. OrderedDict Rewrite: Start with Exercise 6.4 (page 108), where you used a standard dictionary to represent a glossary. Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary
'''

# From 6.4 

from collections import OrderedDict

class ProgrammingGlossary:
    programming_words = OrderedDict([
        ("Print Statements", "Prints anything"),
        ("if-else", "Use for condition"),
        ("List", "Use for storing the list"),
        ("Loop", "Use for efficient program"),
        ("Boolean", "Use for true or false statements"),
        ("Function", "A block of organized, reusable code"),
        ("Dictionary", "A collection of key-value pairs"),
        ("Module", "A file containing Python definitions and statements"),
        ("Exception", "An event that occurs during the execution of a program"),
        ("Tuple", "An immutable, ordered collection of elements")
    ])

    def display_glossary(self):
        for word, meaning in self.programming_words.items():
            print(f"{word} meaning -\n{meaning}\n")

# Create an instance of ProgrammingGlossary
glossary_instance = ProgrammingGlossary()

# Call the method to display the glossary
glossary_instance.display_glossary()
