# 6. Write a program to calculate the factorial of a given number using for loop

# Solution:
num = int(input("Enter the number: "))
fact = 1
for i in range(1, num+1):
    fact *= i