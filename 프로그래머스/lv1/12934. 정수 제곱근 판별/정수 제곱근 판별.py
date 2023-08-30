def solution(n):
    num = n ** 0.5  #n의 제곱근 num
    
    if num == int(num): #n의 제곱근이 정수라면
        return ((num+1) ** 2)
    else:
        return -1




'''

def solution(n):
    answer = 0
    num = n ** 0.5
    
    if num == int(num):
        answer = (num+1) ** 2
    else:
        return -1
    return answer
    
def solution(n):
    #x+1의 제곱 or -1을 저장할 변수
    answer = 0
    #양의 정수 n의 제곱근을 저장하는 변수
    x = n ** 0.5
    
    #n이 양의 정수 x의 제곱이라면
    if str(x)[-2:] == '.0':
        #x+1의 제곱을 리턴
        answer = (x + 1) ** 2
    #n이 양의 정수 x의 제곱이 아니라면
    else:
        #-1을 리턴
        answer = -1
    
    return answer
    
    
def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1
'''