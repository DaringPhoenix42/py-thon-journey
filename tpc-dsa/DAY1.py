# #Sum of two digit number
# no = int(input("Enter a two digit number:"))
# n1= no%10
# n2=no//10
# res = n1+n2
# print("The sum of two digit number is:",res)

# #Sum of three digit number
# no = int(input("Enter a two digit number:"))
# n1= no%10
# no=no//10
# n2 = no%10
# no= no//10
# n3= no%10
# res = n1+n2+n3
# print("Sum of  digits of three digit  number:",res)

#Sum of six digit number
# no = int(input("Enter a six digit number:"))
# n1= no%10
# no=no//10
# n2 = no%10
# no= no//10
# n3= no%10
# no=no//10
# n4=no%10
# no=no//10
# n5=no%10
# no=no//10
# n6=no%10
# res = n1+n2+n3+n4+n5+n6
# print("Sum of  digits of six digit  number:",res)

#Reverse of seven digit
# no = int(input("Enter a seven digit number:"))
# n1= no%10
# no=no//10
# n2 = no%10
# no= no//10
# n3= no%10
# no=no//10
# n4=no%10
# no=no//10
# n5=no%10
# no=no//10
# n6=no%10
# no=no//10
# n7=no%10
# res = n1*1000000+n2*100000+n3*10000+n4*1000+n5*100+n6*10+n7*1
# print("rev of  digits of six digit  number:",res)

#find sum of first and last digit number(6)(in 3 steps)
# no = int(input("Enter a six digit no"))
# n1= no%10
# n2= no//100000
# print("Result of sum of first and last digit for six digit number:",n1+n2)

#Fundamental Datatypes
# int
# float 
# double 
# complex
# bool
#  str

# Python does not support primitive datatypes and thus slower than other languages which do support them,Immutability means no change in the same memory or same object.

# Java does memory optimization for same data only for the datatype string similar to python memory optimization that is shared data has only one memory address.

#Complex Datatype support
# a= 1+2j
# b = 2+3j
# print(a+b)
# c= 2
# d= 6
# print(complex(c,d))
# print(complex(True, True))

# Special Operators are of two types Identity and Membership operators
# Identity: is and is not
# a=10
# b=10 
# print(a is b)
# Working: Checks if the compared quantities are referencing the same memory location returns true in this case else false for is.
# Memebership: in, not in
# Working: Checks if an entity is present or not in a collection 

# Math Module
# In python every .py file is considered a module
# useful funcs : sqrt,pi,ceil,floor,power,factorial, trunc, gcd

# Eval Function
# Working : Evaluates expressions and gives output and can take input of other datatypes such as list and tuples.
# res = eval(input('Enter a expression:'))
# print(f'The result is {res}')

# Print function attributes or parameters
# print('hello'+'world')
# print('hello\nWorld')
# print('hello\tworld')
# print('hello'*4)
# print(4*'hello')
# sep parameter for the print function specifies the character to be used as a seperator for printing data
# a,b,c= 10,20,39
# print(a,b,c, sep=':')
# end parameter specifies the value that the print statement should be ended with
# print("hello",end='')
# print('rajesh',end='')

# Formatted string 
# eg %i,d for int datatype  , %s for all datatypes etc
# a=10
# print('A value is %i' %a)
# list =[10,20,30]
# print('list is %s'%list)

# Replacement Operator {}
# name= 'Vijay'
# salary =30000
# print('hello {0}, my salary is {1}'.format(name,salary))
# print('hello {x}, my salary is {y}'.format(x=name,y=salary))

# Accept 5 nos and find max no

# a,b,c,d,e = int(input('Enter the first no:')),int(input('Enter the second no:')),int(input('Enter the third no:')),int(input('Enter the fourth no:')),int(input('Enter the fifth no:'))
# max =a 
# if max<b:
#    max =b
# if max<c:
#     max = c
# if max<d:
#     max = d
# if max<e:
#     max =e
# print("The max no is ", max)

# Accept 5 paper marks, find total and percentage, accept gender if gender is f and per>=82 print she can take admission and if gender is m and per>=62

# a,b,c,d,e,f = int(input('Enter the first no:')),int(input('Enter the second no:')),int(input('Enter the third no:')),int(input('Enter the fourth no:')),int(input('Enter the fifth no:')), input('Enter gender in form f or m:')
# print('The total is',a+b+c+d+e)
# per = (a+b+c+d+e)/5
# if per>=82 and 'f' in f:
#     print('She can take admission')
# elif per>=62 and 'm' in f:
#     print('He can take admission')

# else: print("Admission not permissible")

# WAP to check char is upper, lower, digit or special symbol
# chr function for converting int values to character values
# ord function for converting character to ASCII values
# ch = input('Enter any character:')
# ch =ord(ch)
# if ch>=65 and ch<=90:
#       print('The char entered is uppercase')
# elif ch>=97 and ch<=122:
#     print("The char is lowercase")
# elif ch>=48 and ch<=57:
#     print("digit value")
# else:
#     print("special character")

# WAP to check year is leap year or not
#  Two types of leap years: century  and non century leap year 
# y = int(input('Enter the year:'))
# if  y%400 ==0:
#     print('A  centurian leap year')
# elif y%4 ==0:
#     print('A Non Centurian Leap year')
# else:
#     print('The year is not a leap year')

#
# cp,cat= int(input("Enter the cost price:")),input('Are you a student?: Answer in y/n form:')
# dis =0
# if 'y' in cat and cp>500:
#     dis = 0.1
# 
# if 'n' in cat and cp>500:
#     dis=0.08
# else: dis =0.02
# print(f'Cost price is {cp} and discount rate is {dis*100}% and netprice is {cp-(cp*dis)}')
# Loops
# While loop is used when range is not given and for loop is used when range is given

#reverse the number
# no=int(input("enter any number: "))
# rev=0
# while no>0:
#     rem=no%10
#     rev=rev*10+rem
#     no=no//10
# print("reverse no is ",rev)
#count no. of digits
# no = int(input('Enter the number:'))
# count =0
# sum=0
# prod=1
# while no>0:
#     digit = no%10
#     sum +=digit
#     prod *= digit
#     no=no//10
#     count+=1

# print('The no. of digits is:',count)
# print(f"The product of digits: {prod} and the sum of the digits: {sum}")

# Factorial Code
# factno= int(input('Enter the number for which fact will be computed:'))
def fact(a):
    if a==1 or a==1:
        return 1
    return a*fact(a-1)
# print(f'The factorial of {factno} is {fact(factno)}')
# Loop Code 
# fact =1
# no =factno
# while factno>0:
#     fact *= factno
#     factno -=1
# print(f"The factorial of {no} is {fact}")

#Armstrong Number for any number
# no  = int(input('Enter the no.'))
# c1=no
# c2=no
# count = 0
# arm =0
# sum =0
# while c1>0:
#     c1=c1//10
#     count +=1
# while c2>0:
#     rem = c2%10
#     c2 = c2//10
#     sum += rem**count

# if sum == no:
#     print(f"{no} is an armstrong number")
# else:
#     print(f"{no} is not an armstrong number") 

# for i in range(0,10001):
#     no  = i
#     c1=no
#     c2=no
#     count = 0
#     arm =0
#     sum =0
#     while c1>0:
#         c1=c1//10
#         count +=1
#     while c2>0:
#         rem = c2%10
#         c2 = c2//10
#         sum += rem**count

#     if sum == no:
#         print(f"{no} is an armstrong number")

# Check no is palindrome

# no = int(input("enter the number to check: "))
# copy=no
# rev=0
# while no>0:
#     rem=no%10
#     rev=rev*10+rem
#     no=no//10
# if rev==copy:
#     print("{x} is palindrome".format(x=copy))
# else:
#     print("Not Palindrome")

# Check if no is peterson
# no = int(input('Enter the no. to be checked:'))
# c1= no
# sum=0
# while c1>0:
#     rem = c1%10
#     sum += fact(rem)
#     c1 =c1//10

# while c1>0:
#     rem = c1%10
#     fact=1
#     while rem >0:
#         fact = fact*rem
#         rem=rem-1
#     sum+=fact
#     c1= c1//10
# if sum == no :
#     print('The no is peterson Number ')
# else:
#     print('The no is not peterson')
    
# Check if the number is automorphic
# no = int(input('Enter the number to be checked:'))
# sq =no *no
# c1=no
# count =0
# while c1>0:
#     c1= c1//10
#     count+=1
# rem = sq%10**count
# if rem== no:
#     print(f"{no} is automorhpic")
# else:
#     print("no is not automorphic")
    
# A number has an even no of digits and number can be divided exactly into two parts from the middle after equally dividing the number, sum up the parts and find the square of the sum, if we get the number itself as square given number is a tech number

# no = int(input('Enter the no to be checked:'))
# c1 = no
# square =0
# count =0
# while c1>0:
#     c1= c1//10
#     count += 1
# if count%2 ==0:
#     c1 =no
#     rem = c1%10**(count/2)
#     print(rem)
#     quo = c1//10**(count/2)
#     print(quo)
#     square = (rem+ quo)**2
#     print(square)
#     if square == no:
#         print("The no is a tech number")
#     else:
#         print('The no is not  a tech number')
# else: print('Odd Count')
        
    