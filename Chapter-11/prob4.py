# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def show(self):
        print(f"The complex number is {self.real} + {self.imag}i")
        
c1 = Complex(3, 4)
c2 = Complex(2, 1)
c3 = c1 + c2
c4 = c1 * c2
c3.show()
c4.show()
