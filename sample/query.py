"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit

item_counter_one = 0
item_counter_two = 0


user_name = input("Hello! What is you name: ")
print(f"Hello, {user_name}")

print("(1) List items by warehouse (2) Search an item an place an order (3) Quit")

choice = int(input("Which option do you choose: "))

if choice == 1:
    print("+" * 100)
    print("Items in Warehouse 1")
    print("+" * 100)
    for item in warehouse1:
        print(item)

    print("+" * 100)
    print("Items in Warehouse 2")
    print("+" * 100)
    for item in warehouse2:
        print(item)
elif choice == 2:
    item_name = input("Enter an item name you are looking for in the warehouse: ")

    for item in warehouse1:
        if item == item_name:
            item_counter_one += 1

    for item in warehouse2:
        if item == item_name:
            item_counter_two += 1

    print(f"This item exists {item_counter_one + item_counter_two} time(s)")

    if item_counter_one > 0 and item_counter_two == 0:
        print("It can be found in Warehouse 1")

    if item_counter_one == 0 and item_counter_two > 0:
        print("It can be found in Warehouse 2 ")

    if item_counter_one > 0 and item_counter_two > 0:
        print("It can be found in both Warehouses")
        
        if item_counter_one > item_counter_two:
            print(f"This product is more often in Warehouse 1. It is there {item_counter_one} time(s)")
        else:
            print(f"This product is more often in Warehouse 2. It is there {item_counter_two} time(s)")

    if item_counter_one == 0 and item_counter_two == 0:
        print("This item is not in stock")

    place_order = input("Do you want to place an order for this item (yes/no):")

    if place_order == "no":
        pass
    else:
        amount_item = int(input("How many of that item do you want: "))

        if amount_item <= item_counter_one + item_counter_two:
            print("The order has been placed.")
            print(f"You ordered {item_name} {amount_item} time(s)")
        else:
            print("You exceeded the available amount.")
            max_amount = input("Do you wanna order the maximum amount (yes/no)?: ")
            if max_amount == "yes":
                print(f"The order has been placed. You ordered {item_name} {item_counter_one + item_counter_two} time(s)")

elif choice == 3:
    pass
