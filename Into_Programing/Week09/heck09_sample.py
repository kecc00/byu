"""
File: check09_sample.py
Author: Kevin E. Cruz
"""

friend_list = []

#
while True: 
    friend_name = input("Enter a friend's name or type 'finish' to end: ")

    if friend_name.lower() == 'finish':
        break

    if friend_name.lower() != 'finish':
        friend_list.append(friend_name)

print("List of friends:")
for friend in friend_list:
    print(friend)