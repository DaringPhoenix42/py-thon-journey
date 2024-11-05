# 5. Write a python program that will perform following operations on List
#  Update first element with X value and delete the middle element of list.
#  Find max and min element from the list.
def updateFirstElementAndDeleteMiddleElement(lst):
    x=int(input("Enter the value of X: "))
    lst[0]=x
    print(f"List after updating first element with X ={x}: \nFinal list{lst} ")
    if len(lst)%2==0:
        del lst[len(lst)//2]
    else:
        del lst[(len(lst)//2)+1]
        
    print(f"List after deleting middle element: \nFinal list{lst} ")
    
def findMaxAndMinElement(lst):
    max_element = max(lst)
    min_element = min(lst)
    print(f"Max element in the list is: {max_element}")
    print(f"Min element in the list is: {min_element}")
    
def main():
    lst = [10, 20, 30, 40, 50, 60]
    updateFirstElementAndDeleteMiddleElement(lst)
    findMaxAndMinElement(lst)
    
main()
