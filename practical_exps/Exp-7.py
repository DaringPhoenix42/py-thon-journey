
try:
    a = int(input("Enter the dividend: "))
    b = int(input("Enter the divisor: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        c = a / b
        print(f"The result of {a} divided by {b} is {c}.")
        
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")