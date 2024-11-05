# 8. Write a python program to demonstrate inheritance in Python
class Animal:
    def __init__(self):
        print("Animal created")
    def speak(self):
            print("Animal makes a generic sound")
            
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def speak(self):
        print("Dog says Woof!")
        
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")
    def speak(self):
        print("Cat says Meow!")
        
d = Dog()
d.speak()
c = Cat()
c.speak()

        