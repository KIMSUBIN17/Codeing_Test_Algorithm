def solution(n):
    list = []
    for i in range(0,n+1): 
        if i % 2 == 0:
            list.append(i)
    answer = sum(list)
    return answer

'''
def solution(n):
    return sum([i for i in ragne(2,n+1,2)])
    
def solution (b):
    s = 0       //저장공간
    for  i in ange(n+1):
        if i %  2 ==  0:
            s =+ i
    return s

'''