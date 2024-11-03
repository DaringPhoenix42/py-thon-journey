

def copy_file_content(source,destination):
    f=open(source,"r")
    content=f.read()
    f.close()
    f=open(destination,"w")
    f.write(content)
    f.close()
    print("File content copied successfully")
    
def append_data_to_file(file_name,data):
    f=open(file_name,"a")
    f.write(data)
    f.close()
    print("Data appended successfully")
    
def display_file_content(file_name):
    f=open(file_name,"r")
    print(f.read())
    f.close()
    
def main():
    while True:
        print("Menu")
        print("1. Copy file content")
        print("2. Append data to file")
        print("3. Display file content")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        
        if choice==1:
            source=input("Enter source file name: ")
            destination=input("Enter destination file name: ")
            copy_file_content(source,destination)
        elif choice==2:
            file_name=input("Enter file name: ")
            data=input("Enter data to be appended: ")
            append_data_to_file(file_name,data)
        elif choice==3:
            file_name=input("Enter file name: ")
            display_file_content(file_name)
        elif choice==4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        print("\n")
        
main()
        
    