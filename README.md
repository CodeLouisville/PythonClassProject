# Week 2 Challenge Code Louisville 2017 Python/Django Cohort

The last challenge focused on using standard Python functions and datastructures to allow a user to build a menu from the command line. What if however a user needed to be able to create menus for multiple restaurants, and what if those restaurants each had different setups? Our data structures and functions could quickly become deeply nested and overly complex. This week we will introduce and use Classes to help manage some of that complexity.

## Challenge:
Louies Pizza is growing. It now has sit down, drive thru, carry out and delivery locations. Create a command line script that allows a user to create an instance of their restaurant while keeping in mind that not every restaurant will have the same needs. Along with this each location should be able to create a menu with all the functionality from week 1 specific to their location.

Restaurant Requirements:
Name
Address
Type

Each type of location will then have specific data associated with it:
Drive Thru: 
Number of lanes
Number of Windows (1 or 2 for payment and handing out food)

Delivery:
Driver Count
Delivery Radius
Dispatch Time - function that captures when the last driver left

Carry Out:
Register Count

Dine In:
Table Count
Waiter Count
Register Count

A user should also be able to update any of the values for their location as well as quickly view them.

## Tips:
[Classes](https://docs.python.org/3/tutorial/classes.html)

    class Location(object):
        def __init__(self, name, address, location_type):
            self.name = name
            self.address = address
            self.location_type = location_type
            self.menu = {}

        def show_menu(self):
            print(self.menu)

[Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

    class Carry_Out_Location(Location):
        def __init__(self, name, address, location_type, register_count):
            super().__init__(name, address, location_type)
            self.register_count = register_count

        def __str__(self):
            print(self.name)

You built a function based solution for storing menus last week. Look at adding that functionality as methods on your parent location class so that all locations can create a menu without duplicating your menu functionality 4 times. 

## Solution
There are a variety of ways to approach this problem in Python each with it's own merits and complexities. For one example see the locations.py solution in this project.

## Additional Notes
test_instances.txt contains a set of example instances you can put in start.py to prevent starting with no data/instances each time you run the script.
