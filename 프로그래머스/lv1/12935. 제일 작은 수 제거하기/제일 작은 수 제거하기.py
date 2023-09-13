def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]


'''
def solution(arr):
    if len(arr) > 1:  
        arr.remove(min(arr))
        return arr    
    else:   #빈 배열인 경우 
        return [-1]
    
    
    


'''