a=10
b=11
c=12
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print("The greatest number is: ",greatest(a,b,c))