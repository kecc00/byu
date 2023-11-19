"""
File: checkpoint.py
Author: Kevin E. Cruz
"""

def print_shopping_list(items):
    print("\nThe shopping list is:")
    for item in items:
        print(item)

    print("\nThe shopping list with indexes is:")
    for idx, item in enumerate(items):
        print(f"{idx}. {item}")

def main():
    shopping_list = []
    while True:
        item = input("Item: ")
        if item.lower() == "quit":
            break
        shopping_list.append(item)

    print_shopping_list(shopping_list)

    if shopping_list:
        idx_to_change = int(input("\nWhich item would you like to change? "))
        if 0 <= idx_to_change < len(shopping_list):
            new_item = input("What is the new item? ")
            shopping_list[idx_to_change] = new_item
            print_shopping_list(shopping_list)
        else:
            print("Invalid index, no item changed.")

if __name__ == "__main__":
    main()
