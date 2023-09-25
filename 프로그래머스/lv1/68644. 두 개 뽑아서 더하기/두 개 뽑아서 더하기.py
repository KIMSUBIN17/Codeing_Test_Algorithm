def solution(numbers):
    l=len(numbers)
    answer = []
    index=0
    for i in range(l-1):
        for j in range(i+1, l):
            answer.append(numbers[i] + numbers[j])
            
    answer=list(set(answer))
    answer.sort()
    return answer