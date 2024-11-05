class student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}")
        
d=student(1,"John",90)
d.display()