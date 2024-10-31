marks={
    'John': 90,
    'Jane': 89,
    'Jack': 85
}
print(marks,type(marks))
print(marks['John'])
print(marks.get('Jane'))
print(marks.get('Jill'))
#items
print(marks.items())
#keys
print(marks.keys())
#values
print(marks.values())
#update
marks.update({'Jill': 92, 'Jack': 87, 'John': 91,})
print(marks)
#pop
print(marks.pop('Jack'))