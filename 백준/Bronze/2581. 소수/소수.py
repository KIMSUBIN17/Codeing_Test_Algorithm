M = int(input())        # M 이상의 자연수
N = int(input())        # N 이하의 자연수

answer = []
for i in range(M,N+1):        # M부터 N까지 반복
    for j in range(2,i+1):        # 1은 소수가 아니므로 2부터 시작해서 자기 자신까지 반복할 수 j를 구
        if j== i:                #j와 i가 같다면 소수이므로 answer 리스트에 추가
            answer.append(i)
        if i % j == 0:            #같지않다면 i를 j에 나눈 나머지를 비교해서 나누어 떨어지면 소수가 아니므로 break로 빠져나옴
            break
            
if not answer:        # 아무것도 없는 경우 -1 출력
    print(-1)    
else:
    print(sum(answer))
    print(answer[0])
