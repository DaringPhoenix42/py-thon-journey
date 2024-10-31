a1=int(input("Enter the first number:-"))
a2=int(input("Enter the second number:-"))
a3=int(input("Enter the third number:-"))
a4=int(input("Enter the fourth number:-"))
if a1>a2 and a1>a3 and a1>a4:
    print("The number",a1,"is the greatest")
elif a2>a1 and a2>a3 and a2>a4:
    print("The number",a2,"is the greatest")
elif a3>a1 and a3>a2 and a3>a4:
   print("The number",a3,"is the greatest")
else:
    print("The number",a4,"is the greatest")

