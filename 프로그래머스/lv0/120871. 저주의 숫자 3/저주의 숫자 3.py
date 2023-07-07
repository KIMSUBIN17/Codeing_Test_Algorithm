def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
    return answer

'''
정수n만큼 for문 돌면서,
3으로 나누어 떨어지거나(=3의배수) or 문자에 3이 포함되면 1을 한번 더해줌(해당숫자 건너뛰기위해)
'''


'''
다른 풀이
def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while True:
            if str(answer).count("3") > 0:
                answer += 1
            elif answer%3 == 0:
                answer += 1
            else:
                break

    return answer

'''