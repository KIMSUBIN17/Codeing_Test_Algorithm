#테스트 케이스 수  입력받기
T = int(input())

#각 테스트 케이스 처리
for _ in range(T):
    #배열 A 입력 받기
    A = list(map(int, input().split()))
    
    #배열을 정렬하고 3번째로 큰 값 출력
    A.sort(reverse = True)
    print(A[2])
             
    