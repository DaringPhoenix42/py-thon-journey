
def seprate_even_odd():
    even=[]
    odd=[]
    n=int(input("Enter the number of elements:"))
    for i in range(n):
        num=int(input("Enter the number:"))
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    print("Even list:",even)
    print("Odd list:",odd)
def merge_sort(even,odd):

    print("Even list:",even)
    print("Odd list:",odd)
    even.sort()
    odd.sort()
    print("Sorted even list:",even)
    print("Sorted odd list:",odd)
def update_delete(even,odd):
    even[0]=10
    odd.pop(2)
    print("Updated even list:",even)
    print("Odd list:",odd)
def find_max_min(even,odd):
        print("Max element in even list:",max(even))
        print("Min element in even list:",min(even))
        print("Max element in odd list:",max(odd))
        print("Min element in odd list:",min(odd))
def add_names(even,odd):
    names = input("Enter names separated by space: ")
    names = names.split()
    even.extend(names)
    odd.extend(names)
    print("Updated even list:", even)
    print("Updated odd list:", odd)
    if 'python' in even:
        print("Word python is present in even list")
    else:
        print("Word python is not present in even list")
        # Main function
def main():
    
    while True:
        print("1. Separate even and odd numbers")
        print("2. Merge sort even and odd list")
        print("3. Update and delete elements from even and odd list")
        print("4. Find max and min element in even and odd list")
        print("5. Add names to even and odd list")
        print("6. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
             seprate_even_odd()
        elif choice==2:
            even=[2,4,6,8,10]
            odd=[1,3,5,7,9]
            merge_sort(even,odd)
        elif choice==3:
            even=[2,4,6,8,10]
            odd=[1,3,5,7,9]
            update_delete(even,odd)
        elif choice==4:
            even=[2,4,6,8,10]
            odd=[1,3,5,7,9]
            find_max_min(even,odd)
        elif choice==5:
            even=[2,4,6,8,10]
            odd=[1,3,5,7,9]
            add_names(even,odd)
        elif choice==6:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            if __name__ == "__main__":
                main()
                

main()
                
                
        
        