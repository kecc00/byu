"""
File: shopping_cart.py
Author: Kevin E. Cruz
"""

# Initialize empty list to store shopping cart items
shopping_cart = []

# Display the welcome message
print("Welcome to the Shopping Cart Program!")

# Function to display the menu
def display_menu():
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Function to add an item to the shopping cart
def add_item():
    item = input("What item would you like to add? ")
    shopping_cart.append(item)
    print(f"'{item}' has been added to the cart.\n")

# Function to view the contents of the shopping cart
def view_cart():
    if shopping_cart:
        print("The contents of the shopping cart are:")
        for item in shopping_cart:
            print(item)
    else:
        print("Your shopping cart is empty.")

# Function to remove an item from the shopping cart
def remove_item():
    if shopping_cart:
        print("The contents of the shopping cart are:")
        for i, item in enumerate(shopping_cart, start=1):
            print(f"{i}. {item}")
        index = int(input("Enter the number of the item to remove: "))
        if 1 <= index <= len(shopping_cart):
            removed_item = shopping_cart.pop(index - 1)
            print(f"'{removed_item}' has been removed from your shopping cart.\n")
        else:
            print("Invalid item number. Please try again.")
    else:
        print("Your shopping cart is empty.")

# Function to compute the total (here, just the number of items)
def compute_total():
    total_items = len(shopping_cart)
    print(f"The total number of items in your shopping cart is: {total_items}\n")

# Main program loop
while True:
    display_menu()
    action = input("Please enter an action: ")

    if action == '1':
        add_item()
    elif action == '2':
        view_cart()
    elif action == '3':
        remove_item()
    elif action == '4':
        compute_total()
    elif action == '5':
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
