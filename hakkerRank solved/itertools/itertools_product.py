# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))

final= (list(product(list1,list2)))
for num1,num2 in final:
    print(f"({num1}, {num2})",end=" ")