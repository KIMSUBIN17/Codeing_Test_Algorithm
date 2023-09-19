def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer


'''
1. 0~9 중에서 반복돌려서 numbers에 없는 숫자 찾아서 answer에 더함
'''
