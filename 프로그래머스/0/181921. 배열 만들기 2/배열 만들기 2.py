def solution(l, r):
    answer = []
    for i in range(l, r+1):
        #0과 5를 제외한 숫자가 없을 경우 = 0이나 5만 있을 경우 출력
        if '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '4' not in str(i) and '6' not in str(i) and '7' not in str(i) and '8' not in str(i) and '9' not in str(i) :
            answer.append(i)
    return [-1] if not answer else answer


'''
#다른 풀이 : set 교집합 사용
def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if not set(str(i)) - set(['0', '5']):
            answer.append(i)
    return answer if answer else [-1]
'''