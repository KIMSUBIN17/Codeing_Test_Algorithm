t = int(input())            #테스트케이스 수 입력

for i in range(t):
    ans = []
    n = int(input())        #숫자 n 입력
    
    while n>= 1:           #숫자 n을 이진수로 변환
        ans.append(n % 2)
        n = n //2
        
    for j in range(len(ans)):
        if ans[j]== 1:            #1일 경우 그 위치 j를 출력
            print(j, end = " ")
