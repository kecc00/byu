"""
File:teamactivity02.py
"""

# Create a list to store account details
accounts = []

# Function to display account information
def display_accounts():
    print("\nAccount Information:")
    for idx, (account, balance) in enumerate(accounts):
        print(f"{idx}. {account} - ${balance:.2f}")

# Function to calculate total balance
def calculate_total():
    return sum(balance for _, balance in accounts)

# Function to find the account with the highest balance
def get_highest_balance():
    max_balance = max(accounts, key=lambda x: x[1])
    return max_balance

# Input loop to gather account details
while True:
    name = input("What is the name of this account? (Type 'quit' when done): ")
    if name.lower() == 'quit':
        break
    balance = float(input("What is the balance? "))
    accounts.append((name, balance))

# Display account information, total, and average balances
display_accounts()
total_balance = calculate_total()
average_balance = total_balance / len(accounts) if len(accounts) > 0 else 0

print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")

# Find and display the account with the highest balance
highest_balance_account = get_highest_balance()
print(f"Highest balance: {highest_balance_account[0]} - ${highest_balance_account[1]:.2f}")

# Update accounts if needed
update_account = input("\nDo you want to update an account? (yes/no) ").lower()

while update_account == 'yes':
    display_accounts()
    idx = int(input("What account index do you want to update? "))
    new_amount = float(input("What is the new amount? "))
    accounts[idx] = (accounts[idx][0], new_amount)
    display_accounts()
    update_account = input("\nDo you want to update another account? (yes/no) ").lower()

print("\nFinal Account Information:")
display_accounts()
