f=open("myfile.txt","r")
data=f.readlines()
print(data)
for line in data:
    print(line)
f.close()
