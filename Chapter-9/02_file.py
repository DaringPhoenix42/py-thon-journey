str =" hey this is a file"
f=open("myfile.txt","w")
f.write(str)
f.close()
f=open("file.txt","r")
print(f.read())
f.close()