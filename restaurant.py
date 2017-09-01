import pdb
import datetime
from time import sleep

class Restaraunt(object):
    def __init__(self, name, address, location_type):
        self.name = name
        self.address = address
        self.location_type = location_type
        self.menu = {}

    def __str__(self):
        return str("{0} is located at {1}".format(self.name, self.address))

    def menu_options(self):
        print("\nHow would you like to change this locations menu?")
        print("1. Add an item\n2. Search for an item\n3. Update an item\n4. See the menu\n5. Delete menu\n6. Exit")
        user_choice = input(": ")
        try:
            val = int(user_choice)
            if val == 1:
                self.add_item()
            elif val == 2:
                self.search_item()
            elif val == 3:
                self.update_item()
            elif val == 4:
                self.print_menu()
            elif val == 5:
                self.clear_menu()
            else:
                raise ValueError
        except ValueError:
            print("\t\t\tThat is not a valid option.\n\n\n\n\n")
        finally:
            if val == 6:
                return
            else:
                self.menu_options()

    def add_item(self):
        menu_item = {}
        try:
            category = input("Which menu category should this item be in? ex: Appetizer\n")
            menu_item_name = input("What is the name of the new menu item? \n")
            menu_item_price = input("What is the price of the menu item?\n")
            new_item = {menu_item_name: menu_item_price}
            #pdb.set_trace()
            if category in self.menu:
                self.menu[category].append(new_item)
            else:
                self.menu[category] = [new_item]
        except Exception as e:
            print(e)
            sleep(2)

    def update_item(self):
        lookup = input("Which item do you want to update?\n:")
        try:
            for category, menu_items in self.menu.items():
                for menu_item in menu_items:
                    for name, price in menu_item.items():
                        if lookup == name:
                            updt = input("Would you like to update the price or name?\n")
                            if updt.lower() == "name":
                                new_name = input("What should the new name be?\n")
                                menu_item[new_name] = menu_item.pop(name)
                                print("Menu item name updated.")
                                return
                            elif updt.lower() == "price":
                                new_price = input("What should the new price be?\n")
                                menu_item[name] = new_price
                                print("Menu item price updated.")
                            else:
                                raise ValueError
        except KeyError:
            print("That menu item does not exist yet, you can add it though.\n")
        except ValueError:
            print("That is not a valid option to update.\n")


    def search_item(self):
        lookup = input("Which item are you looking for?\n:")
        try:
            for category, menu_items in self.menu.items():
                for menu_item in menu_items:
                    for name, price in menu_item.items():
                        if lookup in name:
                            print("Item found! The details are:\nName: {0}\nPrice: ${1}\n".format(name, price))
        except KeyError:
            print("That menu item does not exist yet, you can add it though.")

    def print_menu(self):
        if not self.menu:
            print("Menu is empty.")
        else:
            for category, menu_items in self.menu.items():
                print("\n{0}".format(category))
                #pdb.set_trace()
                for menu_item in menu_items:
                    for name, price in menu_item.items():
                        print("{0} ${1}".format(name, price))

    def clear_menu(self):
        self.menu.clear()
        print("Menu cleared!")

class Carry_Out_Restaraunt(Restaraunt):
    def __init__(self, name, address, location_type, register_count):
        super().__init__(name, address, location_type)
        self.register_count = register_count

    def __str__(self):
        return "{0} is located at {1} with {2} registers".format(self.name, self.address, self.register_count)

class Dine_In_Restaraunt(Restaraunt):
    def __init__(self, name, address, location_type, register_count, waiter_count, table_count):
        super().__init__(name, address, location_type)
        self.register_count = register_count
        self.waiter_count = waiter_count
        self.table_count = table_count

    def __str__(self):
        return "{0} is located at {1} with {2} registers. There are {3} tables with a total of {4} individuals on the wait staff".format(self.name, self.address, self.register_count, self.table_count, self.waiter_count)

class Drive_Thru_Restaraunt(Restaraunt):
    def __init__(self, name, address, location_type, lane_count, window_count):
        super().__init__(name, address, location_type)
        self.lane_count = lane_count
        self.window_count = window_count

    def __str__(self):
        return "{0} is located at {1} with {2} lanes and {3} service windows".format(self.name, self.address, self.lane_count, self.window_count)

class Delivery_Restaraunt(Restaraunt):
    def __init__(self, name, address, location_type, driver_count, delivery_radius):
        super().__init__(name, address, location_type)
        self.driver_count = driver_count
        self.delivery_radius = delivery_radius
        self.last_delivery_time = None
    
    def __str__(self):
        if self.last_delivery_time:
            return "{0} is located at {1}. It has {2} driver and delivers within {3} miles. The latest delivery was at {4}".format(self.name, self.address, self.driver_count, self. delivery_radius, self.last_delivery_time)
        else:
            print("{0} is located at {1}. It has {2} driver and delivers within {3} miles"
                .format(self.name, self.address, self.driver_count, self. delivery_radius))

    def update_latest_delivery_time(self):
        self.last_delivery_time = datetime.datetime.now()

    def get_latest_delivery_time(self):
        "The latest delivery to go out was at {0}".format(self.last_delivery_time)
