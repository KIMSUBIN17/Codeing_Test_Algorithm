def solution(n):
    answer = 0
    n = str(n)
    for i in n: #문자열 n을 for문 돌면서
        answer += int(i) #각 문자 i를 int정수로 변환해 더함
        #숫자합을 구하기 위해 다시 정수형(int)로 변환한 것
    return answer

'''# pythoninc code
def solution(n):
    return sum([int(i) for i in str(n)])
    
def solution(n):
    answer = sum((map(int,list(str(n)))))
    return answer
'''