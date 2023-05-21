def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

'''
# 다른 사람의 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2))

set() : 집합 자료형 만드는 함수. 중복허용X 순서O
s1과 s2의 중복을 제거하고 &(and)사용해 교집합만 추출해 len으로 교집합의 길이를 return 
'''