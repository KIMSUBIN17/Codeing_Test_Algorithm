# 수의 개수 입력받기 (ex.4)
n = int(input())
#n개의 수 입력받기 (ex. 1 3 5 7)
numbers = list(map(int,input().split()))
#소수 갯수 저장할 변수
prime_cnt = 0 

for num in numbers:
    #1은 소수가 아니므로 pass
    #2부터 해당 숫자 num까지 돌면서 i를 num과 나누어 떨어지는지 검사
    for i in range(2,num+1):
        # 2부터 num까지의 숫자 i로 x를 나누면서 소수 여부 판단
        # num이 i로 나누어 떨어지면(=나머지가 0이면)i는 num의 약수
        if num % i == 0:       
            if num == i:       #num을 i로 나누었을 때 i가 자기자신이면 소수     
                prime_cnt += 1        #소수일때 cnt 1증가
            break
print(prime_cnt)