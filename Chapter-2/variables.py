a=30 
b="hello"
c=3.14
d=True
e=None
print(a)
print(b)

#comparison operator
print(a==30)
print(a!=30)
print(a>30)
print(a<30)
print(a>=30)
print(a<=30)
print(a>=30)

#logical operator 
print(a==30 and b=="hello")
print(a==30 or b=="hello")
print(not a==30)


#Type function and typecasting
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

a=str(a)
print(type(a))
a=int(a)
print(type(a))
a=float(a)
print(type(a))
a=bool(a)
print(type(a))
a=None
print(type(a))

#input function
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(age)
print(name)
print(type(name))
