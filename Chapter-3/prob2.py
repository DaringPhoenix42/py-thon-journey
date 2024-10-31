# name=str(input("Enter your name:-\n"))
# date=str(input("Enter the date:-\n"))
# print(f" Dear {name}\n You are selected\n Date:-{date}")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Dhruv").replace("<|Date|>","Today"))
