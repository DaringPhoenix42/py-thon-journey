def separate_even_odd():
    even = []
    odd = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        num = int(input("Enter the number: "))
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

def merge_sort(even, odd):
    print("Even list:", even)
    print("Odd list:", odd)
    even.sort()
    odd.sort()
    print("Sorted even list:", even)
    print("Sorted odd list:", odd)

def main():
    while True:
        print("1. Separate even and odd numbers")
        print("2. Merge sort even and odd list")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            even, odd = separate_even_odd()
        elif choice == "2":
            # Ensure that even and odd lists are defined before using them
            if 'even' in locals() and 'odd' in locals():
                merge_sort(even, odd)
            else:
                print("Please separate even and odd numbers first.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()


 
# def separate_even_odd():
#     even = []
#     odd = []
#     n = int(input("Enter the number of elements: "))
    
#     for i in range(n):
#         num = int(input("Enter a number: "))
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
            
#     print("Even list:", even)
#     print("Odd list:", odd)
#     return even, odd

# def merge_sort(even, odd):
#     print("Even list before sorting:", even)
#     print("Odd list before sorting:", odd)
    
#     even.sort()
#     odd.sort()
    
#     print("Sorted even list:", even)
#     print("Sorted odd list:", odd)

# def main():
#     even, odd = [], []  # Initialize empty lists to store separated values
    
#     while True:
#         print("\nMenu:")
#         print("1. Separate even and odd numbers")
#         print("2. Sort even and odd lists")
#         print("3. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             # Call the separate_even_odd function and capture the returned lists
#             even, odd = separate_even_odd()
#         elif choice == "2":
#             # Check if lists are empty; prompt user to separate numbers first if they are
#             if not even and not odd:
#                 print("Please separate even and odd lists first by choosing option 1.")
#             else:
#                 merge_sort(even, odd)
#         elif choice == "3":
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please choose a valid option.")

# main()
