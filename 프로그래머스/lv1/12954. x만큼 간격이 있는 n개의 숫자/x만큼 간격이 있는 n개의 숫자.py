def solution(x, n):
    if x == 0:
        return [0]*n    #리스트에 0을 n만큼 채움 [0,0,0...]
    if x>0:
        return [i for i in range(x,x*n+1,x)]
    #x부터 x*n까지 x의 간격으로 i를 내보내서 리스트에 담음
    else:
        return [i for i in range(x,x*n-1,x)]

        
'''
def solution(x, n):
    return [x*i for i in range(1,n+1)]
    
    
def solution(x, n):
    answer = []
    cnt = 0
    
    while len(answer) != n:
        cnt += 1
        answer.append(x * cnt)
    
    return answer    
'''
    