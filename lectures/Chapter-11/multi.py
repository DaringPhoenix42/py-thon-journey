class employee:
       a=1
       def __init__(self):
               print("Employee is created")
    
class programmer(employee):
        b=2
        def __init__(self):
                super().__init__()
                print("Programmer is created")
class manager(programmer):
         c=3
         def __init__(self):
                super().__init__()
                print("Manager is created")
         
m=manager()
print(m.a)
print(m.b)
print(m.c)
          