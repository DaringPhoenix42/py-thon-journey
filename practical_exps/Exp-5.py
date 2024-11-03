

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")
        
def main():

    s1 = Student("John", 1, 90)
    s2 = Student("Emma", 2, 85)
    s3 = Student("Oliver", 3, 95)
    

    s1.display()
    s2.display()
    s3.display()
    


        