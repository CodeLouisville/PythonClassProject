# activate_this = '/Users/alex/env/Scripts/bin/activate_this.py'
# with open(activate_this) as f:
#     exec(f.read(), {'__file__': activate_this})
    
"""
A basic command line utility that allows somebody to create, update and output a restaurant food menu.
1. Needs to allow for users to add menu items, assign a category, and a price
2. Need to be able to update menu items after they are entered
3. Need to be able to print out the menu to the command line
"""

import pdb
from time import sleep

#A dictionary makes sense for our categories so we can associate keys(categories) and values(menu items)
menu = {}

#We want to capture all the details of the menu item every time, let's use a namedtuple to define what that looks like
menu_item = {}

#Ok, so now let's capture a users menu creation from the command line.
def main_menu():
    print("\nWhat would you like to do?")
    print("1. Add an item\n2. Search for an item\n3. Update an item\n4. See the menu\n5. Delete a menu\n6. Exit")
    user_choice = input(": ")
    try:
        val = int(user_choice)
        if val == 1:
            add_item(menu, menu_item)
        elif val == 2:
            search_item(menu)
        elif val == 3:
            update_item(menu)
        elif val == 4:
            print_menu(menu)
        elif val == 5:
            clear_menu(menu)
            main_menu()
        elif val == 6:
            exit()
        else:
            print("That is not a valid option")
            main_menu()
    except ValueError:
        print("\t\t\tThat wasn't an option!\n\n\n\n\n")
        main_menu()

def add_item(menu, menu_item):
    try:
        category = input("Which menu category should this item be in? ex: Appetizer\n")
        menu_item_name = input("What is the name of the new menu item? \n")
        menu_item_price = input("What is the price of the menu item?\n")
        new_item = {menu_item_name: menu_item_price}
        #pdb.set_trace()
        if category in menu:
            menu[category].append(new_item)
        else:
            menu[category] = [new_item]
    except Exception as e:
        print(e)
        sleep(2)
    main_menu()

def update_item(menu):
    lookup = input("Which item do you want to update?\n:")
    try:
        for category, menu_items in menu.items():
            for menu_item in menu_items:
                for name, price in menu_item.items():
                    if lookup == name:
                        updt = input("Would you like to update the price or name?\n")
                        if updt.lower() == "name":
                            new_name = input("What should the new name be?\n")
                            menu_item[new_name] = menu_item.pop(name)
                            print("Menu item name updated.")
                            main_menu()
                        elif updt.lower() == "price":
                            new_price = input("What should the new price be?\n")
                            menu_item[name] = new_price
                            print("Menu item price updated.")
                            main_menu()
                        else:
                            raise ValueError
    except KeyError:
        print("That menu item does not exist yet, you can add it though.\n")
        main_menu()
    except ValueError:
        print("That is not a valid option to update.\n")
        main_menu()

def search_item(menu):
    lookup = input("Which item are you looking for?\n:")
    try:
        for category, menu_items in menu.items():
            for menu_item in menu_items:
                for name, price in menu_item.items():
                    if lookup in name:
                        print("Item found! The details are:\nName: {0}\nPrice: ${1}\n".format(name, price))
                        main_menu()
    except KeyError:
        print("That menu item does not exist yet, you can add it though.")
        main_menu()

def print_menu(menu):
    if not menu:
        print("Menu is empty.")
    else:
        for category, menu_items in menu.items():
            print("\n{0}".format(category))
            #pdb.set_trace()
            for menu_item in menu_items:
                for name, price in menu_item.items():
                    print("{0} ${1}".format(name, price))
    main_menu()

def clear_menu(menu):
    menu.clear()
    print("Menu cleared!")

if __name__ == "__main__":
    main_menu()
