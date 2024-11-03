class programmer:
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("Programmer created")
    def printDetails(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}")

harry=programmer("Harry",100000,"Python")
rohan=programmer("Rohan",200000,"Java")
harry.printDetails()
rohan.printDetails()
        