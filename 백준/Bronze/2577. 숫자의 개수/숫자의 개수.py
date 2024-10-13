a = int(input())
b = int(input())
c = int(input())

#A,B,C숫자를  int로 받아서 result리스트에 넣음
result = list(str(a*b*c))

#리스트의 값 중에서 1~10의 숫자가 있으면 cnt 값 +1
#1이 끝나면 2가 시작될 때 cnt 를 0으로 초기화
for i in range(0,10):
    cnt = 0
    for num in result:
        if i == int(num):
            cnt += 1
    print(cnt)