class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        
        
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")
        
class pets(Animal):
            def __init__(self, name, age, species, breed):
                super().__init__(name, age, species)
                self.breed = breed
                
            def show(self):
                print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}, Breed: {self.breed}")
class Dog(pets):
    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species,breed)
        self.breed = breed  
    def bark(self):
            print("Woof Woof")
        
    def show(self):
                print(f"Name: {self.name}, Age: {self.age}, Species: {self
              .species}, Breed: {self.breed}")

            
dog1 = Dog("Tommy", 5, "Dog", "Pug")
dog1.show()
dog2 = Dog("Spike", 3, "Dog", "German Shepherd")
dog2.show()
dog3 = Dog("Bella", 2, "Dog", "Golden Retriever")
dog3.show()
dog1.bark()

    