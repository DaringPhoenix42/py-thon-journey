f=open("file.txt","r")
data=f.read()
print(data)


#using with statement
with open("file.txt","r") as f:
    data=f.read()
    print(data)