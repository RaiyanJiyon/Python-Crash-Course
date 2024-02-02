# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

programming_words = {
    "Print Statements": "Prints anything",
    "if-else": "Use for condition",
    "List": "Use for storing the list",
    "Loop": "Use for efficient program",
    "Boolean": "Use for true or false statements",
    "Function": "A block of organized, reusable code",
    "Dictionary": "A collection of key-value pairs",
    "Module": "A file containing Python definitions and statements",
    "Exception": "An event that occurs during the execution of a program",
    "Tuple": "An immutable, ordered collection of elements"
}

for word, meaning in programming_words.items():
    print(f"{word} meaning -\n{meaning}\n")
