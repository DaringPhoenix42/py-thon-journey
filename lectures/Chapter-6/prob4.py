# 4. Write a program to find whether a given username contains less than 10
# characters or not

# Solution:
username = input("Enter your username: ")
if len(username) < 10:
    print("Username is less than 10 characters.")
else:
 print("Username is 10 characters or more.")
