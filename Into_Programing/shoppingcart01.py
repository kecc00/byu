"""
File: shoppingcart01.py
Author: Kevin E. Cruz
"""

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item, price):
        self.cart.append((item, price))
        print(f"'{item}' has been added to the cart.")

    def view_cart(self):
        if not self.cart:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i, (item, price) in enumerate(self.cart, start=1):
                print(f"{i}. {item} - ${price:.2f}")

    def remove_item(self, index):
        if 1 <= index <= len(self.cart):
            del self.cart[index - 1]
            print("Item removed.")
        else:
            print("Invalid item index.")

    def apply_buy_one_get_one_free(self, item):
        item_count = sum(1 for cart_item in self.cart if cart_item[0] == item)
        return item_count // 2  # Return the number of items eligible for discount

    def compute_total(self):
        total = sum(item[1] for item in self.cart)

        # Apply buy one get one free discount for 'Milk'
        discount_milk = self.apply_buy_one_get_one_free('Milk')
        milk_price = 0.0
        for index, (item, price) in enumerate(self.cart):
            if item == 'Milk' and discount_milk > 0:
                milk_price += price
                discount_milk -= 1

        total -= milk_price
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

def main():
    cart = ShoppingCart()
    print("Welcome to the Shopping Cart Program!\n")

    while True:
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")

        choice = input("Please enter an action: ")

        if choice == '1':
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{item}'? "))
            cart.add_item(item, price)
        elif choice == '2':
            cart.view_cart()
        elif choice == '3':
            index = int(input("Which item would you like to remove? "))
            cart.remove_item(index)
        elif choice == '4':
            cart.compute_total()
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid action.")

if __name__ == "__main__":
    main()
