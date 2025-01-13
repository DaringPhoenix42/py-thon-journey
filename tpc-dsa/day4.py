#tuple data structure
##it is immutable  
#tuple creation
# l=()
# print(l)
# print(type(l))

# l=tuple()
# print(l)
# print(type(l))
 
# t=(1,123,13,12,3,123)
# print(t)
# print(type(t))

# t=1,123,13,12,3,123
# print(t)
# print(type(t))

# t=eval(input("Enter any: "))
# print(t)
# print(type(t))

"""tuple is immutable"""
#index(),find index of number

#sorted()

# t=(40,10,30,20)
# t1=sorted(t)
# print(t1)
# print(t)

#min() and max() functions:
# t=(40,10,30,20)
# print(min(t))
# print(max(t))

#cmp(a,b)
"""it compares elment of both tuples
if both tuple are equal then return zero
small then -1
large then 1"""


# t=1,123,13,12,3,123
# sum=0
# for x in t:
#     sum+=x
# print(sum)
# print(sum/6)

#set data structure
"""represent group of unique values as a single entity
duplicate are not allowed
insertion order not preserved no slicing"""

# s=set()
# print(s)
# print(type(s))

# s={234,123,12,3,123,123}
# print(s)
# print(type(s))

# s=eval(input("enter any: "))
# print(s)
# print(type(s))

#add(x):
"adds item x to the set"
# s={11,22,33,44,55}
# print(s)
# s.add(444)
# print(s)

#eliminate duplicates present in list
# l=[12,123,123,12,34,45]
# l2=set(l)
# print(list(l2))

#dictionary data structure
'''we use other to respresent group of individual single entity
for key-value pairs go for dictionary
duplicate key not allowed but vale can be duplicated
heterogenous objects allow for both key and value
insertion order is not preserved
mutable,dynamic,indexing slicing not applicable'''

#d={} or d=dict()
# d={}
# print(d)
# print(type(d))

# d=dict()
# print(type(d))

# d={101:"ashish",102:"Raj",103:"Rohit"}
# print(d)
# print(type(d))

# rec={}
# n=int(input("enter no. of students"))
# i=1
# while i<=n:
#     name=input("enter student name")
#     marks=input('enter % marks of student')
#     rec[name]=marks
#     i=i+1
# print(rec)
# for x in rec:
#     print(x,"\t",rec[x])

#updation

# d={100:"Ashish",200:"prashant"}
# print(d)
# d[400]='raj'
# print(d)
# d[100]="john"
# print(d)

"how to delete element in dictionary"
# d={100:"Ashish",200:"prashant"}
# print(d)
# d[400]='raj'
# print(d)
# d[100]="john"
# print(d)
# del d[100]
# print(d)
# d.clear()
# print(d)

#get()

# d={100:"Ashish",200:"prashant"}
# print(d[100])
# print(d.get(100))
# print(d.get(400))#print None
# print(d.get(100,"Guest"))#print default value of key
# print(d.get(400,"Guest"))

#keys():
'it returns all keys assosciated'
# d={100:"Ashish",200:"prashant"}
# print(d.keys())
# for k in d.keys():
#     print(k)

# d={100:"Ashish",200:"prashant"}
# print(d.values())
# for k in d.values():
#     print(k)

#items(),copy()[d.copy()]

# d={100:"Ashish",200:"prashant"}
# for k,v in d.items():#k-->keys,v-->values
#     print(k,'-->',v)

"write a program to take dictionary from keyboard and print sum of values"
# n=int(input("enter no. of pairs"))
# d={}
# i=1

# while i<=n:
#     key=input("enter key: ")
#     value=int(input("enter value: "))
#     d[key]=value
#     i+=1
# print(d)
# sum=0
# for x in d.values():
#     sum+=x
# print(sum)

#check if a key exist in dictionary

# d={"name":"Alice","age":30}
# key=input()
# if d.get(key)!=None:
#     print("Key exists")
# else:
#     print("does not exist")

#write a function to iterate over the keys and values of a dictionary

# d={100:"Ashish",200:"prashant"}
# for k,v in d.items():
#     print(k,end=" ")
#     print(v)

#write a function to merge two dictionaries into a single dictionary
# dict1={100:"Ashish",200:"prashant"}
# dict2={"name":50,"hello":70}
# for x in dict1:
#     dict2[x]=dict1[x] "update() method can be used "
# print(dict2)

#write a function to find the key with a max value in a dictionary
# d={"a":50,"b":70,"c":80,"d":95}
# max=0
# id=0
# for x,v in d.items():
#     if v>max:
#         max=v
#         id=x
# print(id)

# d={100:"Ashish",200:"prashant"}
# d1={}
# for x,v in d.items():
#     d1[v]=x
# print(d1)

# sem=int(input("enter no. of semester"))

# l2=[]
# i=1
# while i<=sem:
#     sub=int(input("enter no. of subject"))
#     l1=[]
#     for j in range(0,sub):
        
#         marks=int(input("enter marks"))
#         l1.append(marks)
#     print(l1)
#     l2.append(max(l1))    
#     i+=1
# print(l2)
# for x in range(0,len(l2)):
#     print("Maximum mark in",x+1,"semester:",l2[x])

# str1=input()
# str2=input()
# l1=[]
# count=0

# for x in str2:
#     if x in str1:
#         continue
#     else:
#       count+=1
# print(count)

#functions
"group of statement repeateadly required"
"reusability is advantage"
# def add():
#     a=int(input("enter first value: "))
#     b=int(input("enter second value: "))
#     res=a+b
#     print("addition is",res)
# add()

#function with parameter no return values
# def add(x,y):
#     res=x+y
#     print("Addition is ",res)
# a=int(input("enter first value: "))
# b=int(input("enter second value: "))
# add(a,b)

#function with parameter with return values
# def add(x,y):
#     res=x+y
#     return res
   
# a=int(input("enter first value: "))
# b=int(input("enter second value: "))
# res= add(a,b)
# print("Addition is ",res)

#can return multiple values in function(arithmatic() function is used)


# def arithmetic(x,y):
#     res1=x+y   
#     res2=x-y   
#     res3=x//y   
#     res4=x*y   
#     return res1,res2,res3,res4

# a=int(input("enter first value: "))
# b=int(input("enter second value: "))
# r1,r2,r3,r4= arithmetic(a,b)
# print("Addition is ",r1)
# print("subtraction is ",r2)
# print("Division is ",r3)
# print("Multiplication is ",r4)
# import sys
# def add(a,b):
#     print("Addition is: ",a+b)
# def sub(a,b):
#     print("Subtraction is: ",a-b)
# def div(a,b):
#     print("Division is: ",a//b)
# def mul(a,b):
#     print("Multiplication is: ",a*b)
# a=int(input("enter a value: "))
# b=int(input("enter b value: "))
# while True:
#     print("1. Add")
#     print("2. Sub")
#     print("3. Mul")
#     print("4. Div")
#     print("0. Exit")
#     n=int(input("Enter any choice: "))
#     if n==1:
#         add(a,b)
#     elif n==2:
#         sub(a,b)
#     elif n==3:
#         mul(a,b)
#     elif n==4:
#         div(a,b)
#     elif n==0:
#         sys.exit(0)
# import sys
# def armstrong(a):
#     li=a
#     arm=0
#     count=0
#     while li<0:
#         li=li//10
#         count+=1
#     l1=a
#     while l1<0:
#         rem=l1%10
#         arm+=rem**count
#         l1=l1//10
#     if arm==a:
#         return True
#     else:
#         return False
# def reverse(a):
#     b=str(a)
#     print(int(b[::-1]))
    
# def div(a,b):
#     print("Division is: ",a//b)
# def mul(a,b):
#     print("Multiplication is: ",a*b)
# a=int(input("enter a value: "))
# b=int(input("enter b value: "))
# while True:
#     print("1. Add")
#     print("2. Sub")
#     print("3. Mul")
#     print("4. Div")
#     print("0. Exit")
#     n=int(input("Enter any choice: "))
#     if n==1:
#         add(a,b)
#     elif n==2:
#         sub(a,b)
#     elif n==3:
#         mul(a,b)
#     elif n==4:
#         div(a,b)
#     elif n==0:
#         sys.exit(0)


"""Types of arguments
1. Positional Arguments--> direct passing value
2. Keyword Arguments add(x=10,y=20) for def add(x,y) x=10,y=20
                     add(y=20,x=33) for def add(x,y) x=33,y=20"""
# def add(x,y):
#     print("X= ",x)
#     print("Y= ",y)
#     print("Result: ",x+y)
# add(x=10,y=20)
# add(y=20,x=33)

"""3. Default Argument"""
# def add(x,y=55):#if value of y is not passed below we should pass here otherwise error
#     print("X= ",x)
#     print("Y= ",y)
#     print("Result: ",x+y)
# add(22)
# add(44,1)#it is taken as default value even y=55 above

"""4. Variable length arguments def f1(*n)"""

# def sum(*n):
#     total=0
#     for n1 in n:
#         total=total+n1
#     print("The sum=",total)
# sum(10)
# sum(10,20)
# sum(10,20,22,66,99,88)

import math
import os
import random
import re
import sys
from datetime import datetime
date_format= "%a %d %b %Y %H:%M:%S %z"

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     d1=datetime.strptime(t1,date_format)
#     d2=datetime.strptime(t2,date_format)
#     diff=abs(d1-d2)
#     return str(int(diff.total_seconds()))
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')
#     fptr.close()



















































