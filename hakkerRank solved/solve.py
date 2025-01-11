# Reading input
no_of_elements = int(input())
set_elements = set(map(int, input().split()))
no_of_command = int(input())

# Processing each command
for _ in range(no_of_command):
    command = input().split()
    action = command[0]
    
    if action == 'pop':
        set_elements.pop() if set_elements else None
    
    elif action in ('remove', 'discard'):
        val = int(command[1])
        if action == 'remove' and val in set_elements:
            set_elements.remove(val)
        elif action == 'discard':
            set_elements.discard(val)

# Output the number of elements left in the set
print(len(set_elements))
