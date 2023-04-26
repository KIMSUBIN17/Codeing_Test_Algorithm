def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


'''
# 코드 더 줄여보기
def solution(strlist):
    return [len(str) for str in strlist]
'''