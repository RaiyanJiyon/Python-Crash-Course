# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n)

programming_words = {
    "Print Statements": "Prints anything",
    "if-else": "Use for condition",
    "List": "Use for storing the list",
    "Loop": "Use for efficient program",
    "Boolean": "Use for true or false statements"
}

print("Print Statements meaning -\n", programming_words["Print Statements"])
print("if-else meaning -\n", programming_words["if-else"])
print("List meaning -\n", programming_words["List"])
print("Loop meaning -\n", programming_words["Loop"])
print("Boolean meaning -\n", programming_words["Boolean"])
