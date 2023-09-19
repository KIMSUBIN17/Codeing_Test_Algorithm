def solution(a, b):
    answer = 0
    for x,y in zip(a,b):
        temp = x*y
        answer += temp   
    
    return answer

'''
def solution (a,b):
return sum([x*y for x,y in zip(a,b)])
'''