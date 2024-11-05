try:
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    if b==0:
        raise Exception("Division by zero")
    else:
        c=a/b
        print(f"The result of {a} divided by {b} is {c}")
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    