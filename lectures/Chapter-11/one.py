# class Employee:
#     campany="Google"
#     Salary=100000
#     def __init__(self,name,age,language):
#         self.name=name
#         self.age=age
#         self.language=language
        
        
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Company: {self.campany}"
    
    
# class coder:
#     def __init__(self, name, age, language, val=None):
#         self.name=name
#         self.age=age
#         self.language=language
#         self.val=val
        
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Language: {self.language}, Salary: {self.salary}"
#     def rating(self):
#         return f"Rating: {self.rating}"
    
    
    
# class Programmer(Employee,coder):
#         company="Microsoft"
#         def __init__(self,name,age,language):
#             # super().__init__(name, age, language)
#                 self.name=name
#                 self.age=age
#                 self.language=language
            
            
            
#         def get_info(self):
#             return f"Name: {self.name}, Age: {self.age}, Company: {self.campany}, Language: {self.language}"
#         def showlangauage(self):
#             return f"language{self.language}"
#         def show_salary(self):
#             return f"Salary:{self.Salary}"
    
# e=Employee("Rahul",25,"Python")
# e1=Programmer("Rohan",25,"Python")
# e2=coder("Rohan",25,"Python",100000)
# print(e.get_info())
# print(e1.get_info())
# print(e1.showlangauage())
# print(e1.show_salary())
# print(e1.rating())





class Employee:
    company = "Google"
    salary = 100000

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Company: {self.company}"


class Coder:
    def __init__(self, name, age, language, salary, rating=None):
        self.name = name
        self.age = age
        self.language = language
        self.salary = salary
        self.rating = rating

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Language: {self.language}, Salary: {self.salary}"

    def get_rating(self):
        if self.rating is not None:
            return f"Rating: {self.rating}"
        else:
            return "No rating available"


class Programmer(Employee, Coder):
    company = "Microsoft"

    def __init__(self, name, age, language, salary=100000, rating=None):
        Employee.__init__(self, name, age, language)
        Coder.__init__(self, name, age, language, salary, rating)

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Company: {self.company}, Language: {self.language}"

    def show_language(self):
        return f"Language: {self.language}"

    def show_salary(self):
        return f"Salary: {self.salary}"


# Creating instances
e = Employee("Rahul", 25, "Python")
e1 = Programmer("Rohan", 25, "Python", 120000, rating=4.5)
e2 = Coder("Rohan", 25, "Python", 100000, rating=3.8)

# Displaying information
print(e.get_info())
print(e1.get_info())
print(e1.show_language())
print(e1.show_salary())
print(e1.get_rating())
