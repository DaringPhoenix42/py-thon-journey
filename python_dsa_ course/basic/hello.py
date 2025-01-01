"""print("Hello")

#number to tell wether it is even odd or negative
num=15
if num>=0:
    print("Postive no:-")
    
    if num%2==0:
     print("Even ")
    else:
     print("Odd")
    
    
else:
    print("Number is negative:-")
    
#leap year or not
year=2024

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"Is aleap year")
        else:
            print(year,"not a leap year")
    else:
        print(year,"Leap year")
else:
    print(year,"Year is not a leap yaer")
    """
#Calculator program simpke calculator:-
print("################################")
num1=int(input("Enter the input1:-"))
num2=int(input("Enter the input2:-"))


while True:
    print("################################")
    print("1.......... Addition...........")
    print("2.......... Multiplication.....")
    print("3.......... Division...........")
    print("4.......... Substraction........")
    print("5.......... floor division......")
    print("6.......... Modular division....")
    choice=int(input("Enter the choice..."))
    if choice==1:
        print(f"{num1}+{num2}={num1+num2}")
        break
    if choice==2:
        print(f"{num1}*{num2}={num1*num2}")
        break
    if choice==3:
        print(f"{num1}/{num2}={num1/num2}")
        break
    if choice==4:
        print(f"{num1}-{num2}={num1-num2}")
        break
    if choice==5:
        print(f"{num1}/{num2}={num1/num2}")
        break
    if choice==6:
        print(f"{num1}%{num2}={num1%num2}")
        break
    
    

    
    