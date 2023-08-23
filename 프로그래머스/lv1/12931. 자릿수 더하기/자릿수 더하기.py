def solution(n):
    answer = 0
    n = str(n)
    for i in n: #문자열 n을 for문 돌면서
        answer += int(i) #각 문자 i를 int정수로 변환해 더함
    return answer

'''# pythoninc code
def solution(n):
    answer = sum((map(int,list(str(n)))))
    return answer
'''