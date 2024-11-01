#degree celsius tomfahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

val1=celsius_to_fahrenheit(0)
val2=fahrenheit_to_celsius(32)
print(val1,val2)
