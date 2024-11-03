
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self, comment=""):
        print(f"This is animal {comment}")
    
    def eat(self, food="generic food"):
        print(f"{self.name} is eating {food}")

class Dog(Animal):
    def speak(self, comment=""):
        if comment:
            print(f"{self.name} says Woof! with a message: {comment}")
        else:
            print(f"{self.name} says Woof!")
        
    def eat(self, food="bones"):
        print(f"{self.name} is eating {food}")

d2 = Animal("bobby")
d2.speak("hi")
d1 = Dog("Tommy")
d1.speak()
d1.speak("I'm happy!")
d1.eat()
d1.eat("meat")



        
        