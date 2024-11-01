class Employee:
    language="Python"
    salary=100000

    def printDetails(self):
        return f"The salary is {self.salary} and the language is {self.language}"
    
    def greet(self):
        return f"Good Morning "

    #object instation

harry=Employee()
rohan=Employee()
rohan.name="Rohan Roro Robinson"
rohan.salary=200000
rohan.language="Java"
print(rohan.name)
print(rohan.language)
print(rohan.salary)

print(harry.language)
print(harry.salary)
#here name is object attribute and language and salary are class attributes
print(harry.printDetails())
print(rohan.printDetails())
print(harry.greet())
print(rohan.greet())