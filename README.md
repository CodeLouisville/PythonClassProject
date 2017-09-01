# Week 1 Challenge

Getting started with Python let's use some standard Python programming concepts such as collections and loops to construct a command line utility that we can create our Louie Pizza food menu with.

## Challenge:
Create a command line script that captures creates a menu by allowing users to add items that have a category and price.
Users should be able to update and search and previously added items and print out the menu items ordered by category.

## Tips:
Python makes it easy to capture user input with the [built-in](https://docs.python.org/3/library/functions.html) [input()](https://docs.python.org/3/library/functions.html#input) function. 

    capture = input("What is your name?\n")
    print(capture)

[Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) are great for Key, Value associations:

    menu = {"Appetizers": "Jalapeno Poppers, Garlic Bread", 
            "Pizza": "Sausage, Pepperoni"}

Loop over items in a dictionary by calling the [dict.items()](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) function in a loop

    for k, v in menu.items():
        print("This is the key: {0} and this is the value {0}"
              .format(k, v))

Try taking the above and putting it in your Python REPL to test out how your loops, data structures and functions work before writing your scripts.

## Solution
There are a variety of ways to approach this problem in Python each with it's own merits and complexities. For one example see the menu.py solution in this project.
