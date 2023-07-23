def solution(start, end):
    answer = []

    for i in range(start,end+1):
        answer.append(i)
    return answer


'''
#짧은풀이

def solution(start, end):
    return [i for i in range(start,end+1)]
    
#다른풀이
def solution(start, end):
    return list(range(start, end + 1))

'''