# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class  Vector:
    def __init__(self, *args):
        self.values = args

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Both vectors must have the same dimension")
        return Vector(*[a + b for a, b in zip(self.values, other.values)])
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.values) != len(other.values):
                raise ValueError("Both vectors must have the same dimension")
            return sum([a * b for a, b in zip(self.values, other.values)])
        else:
            return Vector(*[a * other for a in self.values])
        
    def __str__(self):
        return str(self.values)
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2) 
print(v1 * v2) 

