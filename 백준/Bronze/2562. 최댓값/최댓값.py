li = []
for _ in range(9):
    n = int(input())
    li.append(n)
    
print(max(li))
#리스트에서 가장 큰 수 뽑아서 그 수의 index번호에 +1 한 수를 출력(인덱스번호는 0부터 시작되므로 1을 더함)
print((li.index(max(li)))+1)
