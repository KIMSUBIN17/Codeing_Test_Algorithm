data = []
#x,y값 입력받아 data 리스트에 저장 
for i in range(int(input())):
    x,y = map(int,input().split())
    data.append((x,y))

#y값 우선으로 오름차순 정렬하고, y값이 같다면 x값으로 오름차순 정렬
data.sort(key = lambda x : (x[1], x[0]))

#data리스트 값 출력
for d in data:
    print(d[0], d[1])