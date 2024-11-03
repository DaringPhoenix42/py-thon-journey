
try:
      print("I am in try block")
      a = int(input("Enter the dividend: "))
      print(a)
      
except Exception as e:
        print(e)
finally:
    print("I am in else block")

#finally block will always execute whether there is an exception or not
