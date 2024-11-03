

def add_student(students):
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

def display_python(students):
    found = False
    for student in students:
        if student[1].lower() == 'python':
            print("Roll number:", student[0], "Marks:", student[2])
            found = True
    if not found:
        print("No student found with the name 'Python'.")

def demonstrate_nested_tuple():
    nested_students = (
        ('101', 'Alice', (85, 92, 78)),
        ('102', 'Bob', (76, 85, 90)),
        ('103', 'Charlie', (88, 79, 84)),
        ('104', 'Python', (91, 89, 95)),
        ('105', 'Eve', (77, 88, 91))
    )
    sorted_students = sorted(nested_students, key=lambda x: x[1])
    print("Sorted Students by Name:")
    for roll_number, name, marks in sorted_students:
        print(f"Roll Number: {roll_number}, Name: {name}, Marks: {marks}")

def main():
    students = []
    while True:
        print("1. Add student details")
        print("2. Display student details whose name is Python")
        print("3. Demonstrate nested tuple and sort by name")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_student(students)
        elif choice == 2:
            display_python(students)
        elif choice == 3:
            demonstrate_nested_tuple()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice")
        print("\n")

main()


