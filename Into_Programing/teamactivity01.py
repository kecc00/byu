"""
File: teamactivity01.py
"""

# Create a dictionary to store account names and balances
accounts = {}

# Loop to input account details
while True:
    name = input("Enter the name of this account (Type 'quit' to finish): ")
    if name.lower() == 'quit':
        break
    balance = float(input("What is the balance? "))
    accounts[name] = balance

# Display account information
print("\nAccount Information:")
total_balance = 0

for account, balance in accounts.items():
    print(f"{account} - ${balance:.2f}")
    total_balance += balance

# Calculate and display total and average balances
average_balance = total_balance / len(accounts) if len(accounts) > 0 else 0
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")
