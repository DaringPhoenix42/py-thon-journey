from itertools import groupby

s = input()
s_final = []

for key, group in groupby(s):
    key = int(key)
    s_final.append((len(list(group)), key))
    
print(*s_final)