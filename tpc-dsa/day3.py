# Immutability Concept there are two types of memory: Stack and Heap Memory, python has automatic garbage collection for unused variables and shared memory address for same content in two different variables.
# s = 'ashish'
# s1 = 'raj'
# print(id(s), id(s1))
# a = 10
# b= 10
# print(f'a:memory address:{id(a)} , b memory address :{id(b)}')
# s = "Learning Python is very easy"
# l1 = s.split()
# print(l1)

#  join function used to join lists, tuples of strings using the specified seperator
# print(':'.join(l1))
#  Changing case of strings : upper() , lower(), title(), capitalize() 
#  Checking start and end of a string: startswith() and endswith() case sensitive returns boolean value
# s = "Learning python is very easy"
# print(s.startswith('Learning'))
# print(s.startswith('learning'))
# print(s.endswith('easy'))

# Check type of characters: isalnum(): Checks if string contains numbers and characters
# isdigit() :Checks if the string contains only digits
# isspace() , isalpha()

# Ways to reverse a string
# s = input()
# print(''.join(reversed(s))) 

# s = input()
# i = len(s)-1
# rev =''
# while i>=0:
#     rev = rev + s[i]
#     i-=1
# print(rev)

# # Reverse the string without shortcut and inbuilt function
# s=input()
# rev =''
# for x in s:
#   rev = x + rev
# print(rev)

# s = 'Learning Python is very easy'
# l1 = s.split()
# rev =''
# for x in l1:
#     rev = x+' '+rev 
# print(rev)

# s = "Learning python is very easy"
# l1 = s.split()
# rev =''
# for x in l1:
#     rev = rev +' ' + x[::-1]  
# print(rev)

# s = input()
# s1 =''
# for x in s:
#     if x not in s1:
#         s1 = s1+x
# print(s1)



    # no=input("enter mobile number")
    # if len(no)==10:
    #     if no.isdigit():
    #         if no.startswith('+91'):
    #             print("mobile number is of India")
    #         else:
    #             print("outside number")
    #     else:
    #         print("non digit")
    # else:
    #     print("enter a valid number")


# list: insertion order prserved duplicate objects are allowed
#mutable
# l1=list()
# print(type(l1))

# l1 =eval(input())
# print(type(l1))

# n=[0,1,2,3,4,5]
# i=0
# while i<len(n):
#     print(n[i])
#     i=i+1
# n=[7,8,9,10]
# n.insert(3,"raj")
# print(n)

#extend

# order1=["chicken","pompom","aauaau"]
# order2=["moooo","bhaau","lalala"]
# order1.extend(order2)
# print(order1)

#remove()
# n=[10,20,10,30]
# n.remove(10)
# print(n)
# n.remove(30)
# print(n)
# print(n.pop())
# s=[10,20,30,40]
# print(s.pop())
# print(s)

#reverse
# n=[10,20,30,40]
# n.reverse()
# print(n)

#sort

# n=[20,5,15,10,0]
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)

# n=[123,123,[4242,23,123,1],12,[4,56,6],123,12,3]
# print(n[0])
# print(n[2])
# print(n[4])
# print(n[4][0])
# print(n[4][2])
# for x in n:
#     print(x)

# n=[[10,20,30],[40,50,60],[70,80,90]]
# print(n)
# for x in n:
#     print(x)

# for i in range(len(n)):
#     for j in range(len(n[i])):
#         print(n[i][j],end=" ")
#     print()

# l1=eval(input())
# max=0
# for x in l1:
#     if x>max:
#         max=x
# print(max)

# li=eval(input())
# l2=[]
# for x in li:
#     if x not in l2:
#         l2.append(x)
# print(l2)

# li=eval(input())
# l2=[]
# j=len(li)-1
# while j>=0:
#     l2.append(li[j])
#     j=j-1
# print(l2)

#dupicate value remove
# li=eval(input())
# l2=[]
# comp=0
# for x in li:
#     if x!=comp:
#         l2.append(x)
#     comp=x
# print(l2)


#palindromic list
# li=eval(input())
# l2=[]
# j=len(li)-1
# while j>=0:
#     l2.append(li[j])
#     j=j-1
# print(l2)
# if l2==li:
#     print("palindrome")



# Check if list is palindrome
# l1 = eval(input())
# if l1[::-1] == l1:
#     print("String is palindrome")
# else:
#     print("String is not a palindrome")
# i =0
# mid = (len(l1)/2)-1
# j =len(l1)-1
# while i<mid:
#     while j>mid:
#         if l1[i]!=l1[j]:
#             print("String is not a palindrome")
#             break
#         i += 1
#         j -= 1
# print('String is palindrome')

#common element in two list
# l1=eval(input())
# l2=eval(input())
# l3=[]
# i=0
# while i<len(l1):
#     if l1[i] in l2:
#         l3.append(l1[i])
#     i=i+1
        
# print(l3)

#sum of element of list

# remove an element from a list by value
# l1=eval(input())
# element=int(input())
# l2=[]
# for x in l1:
#     if x==element:
#         continue
#     l2.append(x)
# print(l2)

#find all duplicates in list

# l1=eval(input())
# l2=[]
# l3=[]
# for x in l1:
#     if x not in l2:
#         l2.append(x)
#     else:
#         l3.append(x)
# print(l3)

#anagram strings

# str1=input().upper()
# str2=input().upper()
# str3=''
# for x in str1:
#     if x in str2:
#         str3=str3+x
# if len(str3)==len(str2):
#     print("anagram")
# else:
#     print("no")

#next larger element Input: n=4,arr[]=[1,2,3,4]
#output: 3 4 4 -1

# n= int(input())
# l1=[]
# l2=[]
# for x in range(0,n):
#     a=int(input())
#     l1.append(a)
# for y in range(1,len(l1)):       
#     if l1[y]>l1[y-1]:
#         l2.append(l1[y]) 
#     else:
#         l2.append(l1[y-1])
# l2.append(-1)
# print(l2)

#count number of vowels and string
# str1=input()
# str='aeiouAEIOU'
# count1=0
# count2=0
# for x in str1:
#     if x in str:
#         count1+=1
#     else:
#         count2+=1
# print("vowels are",count1,"and consonants are",count2)

#remove white space
# str1=input()
# str2=''
# for x in str1:
#     if x==" " in str1:
#         continue
#     str2=str2+x
# print(str2)

#count words in string
str1= input()
count=1
for x in str1:
    if x==" ":
        count+=1
print(count)





 