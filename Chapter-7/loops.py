#loops in python
i=0
while i<5:
    print(i)
    i=i+1



# For loop
list=[1,2,3,4,5]
print(type(list))
for item in list:
    print(f"{item}\t")
else:
    print("The loop is completed")

# for loop with range
for i in range(1,10):
    print(i)

#use of continue with for loop and range
for i in range(1,10):
    if i==5:
        continue
    print(i)

#use of break with for loop and range
for i in range(1,10):
    if i==5:
        break
    print(i)