

try:
      print("I am in try block")
      a = int(input("Enter the dividend: "))
      print(a)
      
except Exception as e:
        print(e)
else:
    print("I am in else block")
   
    
    #if successful execution then it will go to else block
    #if there is an exception then it will not go to else block