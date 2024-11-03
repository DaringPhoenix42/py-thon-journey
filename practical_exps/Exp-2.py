# Aim: Write a menu driven python program to check if number and string palindrome and find the factorial of the input number

def isPalindromenum(num):
    
    if str(num)==str(num)[::-1]:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)
    
def isPalindromestr(string):
    if string==string[::-1]:
        print("String is palindrome")
    else:
        print("String is not palindrome")

def main_menu():
    
    while True:
        print("Main Menu")  
        print("1. Check if number is palindrome")
        print("2. Check if string is palindrome")
        print("3. Find factorial of a number")
        print("4. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            num=int(input("Enter a number:"))
            isPalindromenum(num)
        elif choice==2:
            string=input("Enter a string:")
            isPalindromestr(string)
        elif choice==3:
            num=int(input("Enter a number:"))
            factorial(num)
        elif choice==4:
            exit()
        else:
            print("Invalid choice")
        print("\n\n")
        
        
main_menu()
        
        
        