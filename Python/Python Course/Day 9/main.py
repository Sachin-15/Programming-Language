# Python Dictionary


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again",
    123:"the starting three natural Numbers"
    }

# Retrieving the items from the dictionary.
# print(programming_dictionary["Bug"])
# print(programming_dictionary[123])

# Adding new items to dictionary.
programming_dictionary["Algorithm"]="Step by step procedure to solve a particular problem."
# print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])