def solution(n, k):
    answer = []
    
    for i in range(1,n+1):
        if i % k == 0:
            answer.append(i)
        
    return answer

'''
#리스트 컴프리헨션 사용
def solution(n, k):
result = [i for i in range(1, n+1) if i % k == 0]
return result
'''