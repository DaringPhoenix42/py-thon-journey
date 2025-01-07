# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr

S, k = input().split()
merged = cwr(sorted(S), int(k))

for i in merged:
        print(''.join(i))
