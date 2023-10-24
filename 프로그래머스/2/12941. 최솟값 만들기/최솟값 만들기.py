def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer

''' 
# 오답노트 
곱의 누적합이 최소가 되려면 A의 가장 큰 값 * B의 가장 작은 값으로 계산되어야함
A -> 내림차순 정렬, B -> 오름차순 정렬 해줘야함
정렬안하고 그냥 돌리면 입출력 예시2번에서 누적값10이 아닌 11이 나옴(1*3 + 2*4 = 11(X) / 1*4 + 2*3 = 10(O)
'''