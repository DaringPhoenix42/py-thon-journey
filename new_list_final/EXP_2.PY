def checkPallindromeString(string):
    if string==string[::-1]:
        print("String is palindrome")
        
    else:
        print("String is not palindrome")
        
def checkPallindromeNumber(num):
    
    if str(num) == str(num)[::-1]:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
    
def main_menu():
    while True:
        print("Main Menu")
        print("1. Check if number is palindrome")
        print("2. Check if string is palindrome")
        print("3. Exit")
        choice =str(input("Enter your choice:"))
        if choice == '1':
            num = int(input("Enter a number:"))
            checkPallindromeNumber(num)
        elif choice == '2':
            string = input("Enter a string:")
            checkPallindromeString(string)
        elif choice == '3':
            exit()
        else:
            print("Invalid choice")
            
main_menu()
    