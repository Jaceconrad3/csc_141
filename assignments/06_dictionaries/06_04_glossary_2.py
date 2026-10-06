# Jace Conrad
# Chapter 6
# Uses a loop to print a glossary of 10 programming terms and their simple definitions.

glossary = {"variable": "A labeled box where you can save a piece of data to use later.",
    "string": "Just regular text wrapped in quotation marks.",
    "list": "A collection of items kept in a specific order, like a to-do list.",
    "loop": "A way to tell Python to repeat a task over and over automatically.",
    "dictionary": "A collection of key-value pairs used to connect words or info together.",
    "integer": "A whole number without a decimal point, like 5 or -3.",
    "float": "A number that has a decimal point, like 4.5 or 3.14.",
    "boolean": "A value that is either True or False.",
    "comment": "A note written in the code for humans to read that Python ignores.",
    "if statement": "A way for your program to make decisions based on conditions.",}

for word, meaning in glossary.items():
  print(f"{word.title()}:\n{meaning}\n")