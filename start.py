# activate_this = '/Users/alex/env/Scripts/bin/activate_this.py'
# with open(activate_this) as f:
#     exec(f.read(), {'__file__': activate_this})
    
import pdb
from time import sleep
import restaurant

restaurants = {}

def add_restaurant(restaurants):
    name = input("What is the new restaurant name?\n")
    address = input("What is the new restaurant address?\n")
    restaurant_type = input("""What is the new restaurant type?\n\t
    1. Carry Out\n\t
    2. Dine-In\n\t
    3. Drive-Thru\n\t 
    4. Delivery\n""")
    if int(restaurant_type) == 1:
        register_count = input("How many registers does this restaurant have?\n")
        new_restaurant = restaurant.Carry_Out_Restaraunt(name, address, restaurant_type, 
                                                   register_count)
        restaurants[name] = new_restaurant
    elif int(restaurant_type) == 2:
        table_count = input("How many tables does this restaurant have?\n")
        waiter_count = input("How many waiters and waitresses does this restaurant have?\n")
        register_count = input("How many registers does this restaurant have?\n")
        new_restaurant = restaurant.Dine_In_Restaraunt(name, address, restaurant_type, 
                                                 register_count, waiter_count, table_count)
        restaurants[name] = new_restaurant
    elif int(restaurant_type) == 3:
        lane_count = input("How many lanes does this restaurant have?\n")
        window_count = input("How many drive-thru windows does this restaurant have?\n")
        new_restaurant = restaurant.Drive_Thru_Restaraunt(name, address, restaurant_type, 
                                                    lane_count, window_count)
        restaurants[name] = new_restaurant
    elif int(restaurant_type) == 4:
        driver_count = input("How many drivers does this restaurant have?\n")
        delivery_radius = input("How many miles from this restaurant will drivers deliver?\n")
        new_restaurant = restaurant.Delivery_Restaraunt(name, address, restaurant_type, 
                                                  driver_count, delivery_radius)
        restaurants[name] = new_restaurant
    else:
        raise ValueError

def update_restaurant(restaurants):
    #Only updating the basics, you could detect the restaurant type and change the various attributes
    restaurant_name = input("Which restaurant are you looking for?\n")
    try:
        updt_restaurant = restaurants[restaurant_name]
        updt_type = input("What would you like to update the name or address?\n")
        if updt_type.lower() == "name":
            name = input("What is the new name?\n")
            updt_restaurant.name = name
            menu()
        elif updt_type.lower() == "address":
            address = input("What is the new address?\n")
            updt_restaurant.address = address
    except KeyError:
        print("restaurant not found.\n")
        menu()

def menu():
    print("\nWelcome to Louie Pizza's Admin Console.\nWhat would you like to do?\n")
    #pdb.set_trace()
    print('''1. Create a new restaurant \n
2. Search restaurants \n
3. Update a restaurant \n
4. Delete a restaurant \n
5. Interact with a restaurants menu \n
6. Exit\n''')
    user_choice = input(": ")
    try:
        val = int(user_choice)
        if val == 1:
            add_restaurant(restaurants)
            menu()
        elif val == 2:
            restaurant_name = input("Which restaurant are you looking for?\n")
            print(restaurants[restaurant_name])
            menu()
        elif val == 3:
            update_restaurant(restaurants)
            menu()
        elif val == 4:
            restaurant_name = input("Which restaurant do you want to remove?\n")
            #pdb.set_trace()
            del restaurants[restaurant_name]
            menu()
        elif val == 5:
            restaurant_lookup = input("Which restaurants menu do you want to change?\n")
            menu_restaurant = restaurants[restaurant_lookup]
            menu_restaurant.menu_options()
            menu()
        elif val == 6:
            exit()
        else:
            raise ValueError
    except KeyError:
        print("That restaurant does not exist.")
        sleep(2)
        menu()
    except ValueError:
        print("That is not a valid option.\n")
        sleep(2)
        menu()
    except Exception as e:
        print(e)
        sleep(2)
        menu()

if __name__ == "__main__":
    #Add test classes here to preload class instances
    menu()
