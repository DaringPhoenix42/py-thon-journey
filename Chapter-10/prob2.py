class calculator:
    def __init__(self,value):
        self.value=value
    def add(self,num):
        self.value+=num
        return self.value
    def sub(self,num):
        self.value-=num
        return self.value
    def mul(self,num):
        self.value*=num
        return self.value
    def div(self,num):
        self.value/=num
        return self.value
    def __str__(self):
        return str(self.value)
    
cal=calculator(5)
print(cal.add(5))
print(cal.sub(2))
print(cal.mul(3))
print(cal.div(2))
print(cal)


