# Aim: Write a python program to swap two numbers and check if the first number is positive or negative or zero.
# Code:
def swap(a,b):
    print("Before swapping a=",a,"b=",b)
    temp=a
    a=b
    b=temp
    print("After swapping a=",a,"b=",b)
    
def isPostive(a):
    if a>0:
        print("a is positive")
    elif a<0:
        print("a is negative")
    else:
        print("a is zero")
        
a=int(input("Enter a:"))
b=int(input("Enter b:"))
swap(a,b)
isPostive(a)
isPostive(b)