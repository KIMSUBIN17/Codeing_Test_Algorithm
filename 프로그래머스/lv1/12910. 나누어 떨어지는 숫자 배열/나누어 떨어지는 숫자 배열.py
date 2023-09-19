def solution(arr, divisor):
    answer = [] #나누어 떨어지는 숫자들을 담을 정답 배열
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        return [-1] 
    
    return sorted(answer)


'''
def solution(arr, divisor):
    answer = []
    
    #arr에 있는 자연수들을 하나씩 반복
    for num in arr:
        #현재 숫자가 divisor로 나누어 떨어지면
        if num % divisor == 0:
            #answer에 현재 숫자를 넣음
            answer.append(num)
    
    #answer가 빈 리스트라면?
    if answer == []:
        #answer를 -1 하나가 담긴 리스트로 만듦
        answer = [-1]
    #answer가 빈 리스트가 아니라면?
    else:
        #answr의 값들을 오름차순으로 정렬
        answer.sort()
        
    return answer
'''