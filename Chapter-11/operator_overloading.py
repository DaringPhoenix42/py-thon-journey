class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Number(self.value / other.value)
        else:
            raise ValueError("Cannot divide by zero")

    def __str__(self):
        return str(self.value)


num1 = Number(10)
num2 = Number(5)

print(num1 + num2)  # Output: 15
print(num1 - num2)  # Output: 5
print(num1 * num2)  # Output: 50
print(num1 / num2)  # Output: 2.0
