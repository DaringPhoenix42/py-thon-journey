def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)
    
    
input_num = int(input("Enter a number:"))
    
factorial(input_num)