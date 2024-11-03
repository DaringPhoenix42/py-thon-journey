# . Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]
name=input("Enter the name to be searched: ")
for name in l:
    if name[0] == "S":
        print("Hello", name)