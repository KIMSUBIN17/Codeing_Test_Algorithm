def solution(numLog):
    answer = ''
    for i, n in enumerate(numLog[:-1]):
        if numLog[i+1] - n == 1:
            answer += 'w'
        elif numLog[i+1] -n == -1:
            answer += 's'
        elif numLog[i+1] -n == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer
            