li = []
for _ in range(9):
    n = int(input())
    li.append(n)
    
print(max(li))
print((li.index(max(li)))+1)