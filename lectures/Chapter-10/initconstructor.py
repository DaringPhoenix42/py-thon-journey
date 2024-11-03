class Employee:
    language="Python"
    salary=100000
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("Employee created")

    def printDetails(self):
        return f"The salary is {self.salary} and the language is {self.language}"
    @staticmethod
    def greet():
        return f"Good Morning "

    
#object instation
# emp1=Employee()
# emp2=Employee()
# emp2.name="Rohan Roro Robinson"
# emp1.name="Harry"
# print(emp2.name,emp2.language,emp2.salary)
# print(emp1.name,emp1.language,emp1.salary)
# print(emp1.printDetails())
# print(emp2.printDetails())

emp1=Employee("Harry",100000,"Python")
emp2=Employee("Rohan",200000,"Java")
print(emp1.printDetails())
print(emp2.printDetails())
print(emp1.greet())
