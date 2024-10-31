#A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
mess=input("Enter the message: ")
if (p1 in mess) or (p2 in mess) or (p3 in mess) or (p4 in mess):
    print("This is a spam message")
else:
    print("This is not a spam message")

