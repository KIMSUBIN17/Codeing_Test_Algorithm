def solution(x):
    sum = 0     #각 자리수의 합 저장할 변수
    for i in str(x):    #정수x-->문자열x로 변환해 for
        sum += int(i)   #현재 문자를 정수로 변환해 sum에 더함
        
    if x % sum == 0:
        return True
    else:
        return False

'''
def solution(x):
    word = x
    sum = 0
    
    x = list(str(x))
    
    for n in x:
        sum += int(n)
    return word % sum == 0
'''