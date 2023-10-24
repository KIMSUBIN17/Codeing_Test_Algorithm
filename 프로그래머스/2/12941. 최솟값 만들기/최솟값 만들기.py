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

참고링크 
https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-%EC%B5%9C%EB%8C%93%EA%B0%92%EA%B3%BC-%EC%B5%9C%EC%86%9F%EA%B0%92JadenCase-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0%EC%B5%9C%EC%86%9F%EA%B0%92-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python
'''
