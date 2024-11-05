# 6. Write a python program that will perform following operations on Tuples
#  Add and show N student roll number, name and 3 subject marks in a list of tuples.
#  Display student roll number and marks whose name is Python.
def addStudent(students):
    n = int(input("Enter number of students: "))
    for i in range(n):
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = []
        for j in range(3):
            mark = int(input("Enter marks for subject {}: ".format(j+1)))
            marks.append(mark)
        students.append((roll, name, tuple(marks)))
    print("Student list:", students)
    
def displayPython(students):
    found = False
    for student in students:
        if student[1].lower() == 'python':
            print("Roll number:", student[0], "Marks:", student[2])
            found = True
    if not found:
        print("No student found with the name 'Python'.")
            
def main():
    students = []
    while True:
        print("\n1. Add Student")
        print("2. Display Python Students")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addStudent(students)
        elif choice == 2:
            displayPython(students)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            
main()
