def swap(a,b):
    print(f"Before swapping a={a} b={b}")
    temp=a
    a=b
    b=temp
    print(f"After swapping a={a} b={b}")
def ispositive(a):
    if a>b:
        print("a is positive")
    elif a<b:
        print("a is negative")
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
swap(a,b)
ispositive(a)
