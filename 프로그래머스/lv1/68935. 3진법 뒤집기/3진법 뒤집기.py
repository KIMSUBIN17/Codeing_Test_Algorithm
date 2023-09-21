def solution(n):
    answer = ''
    
    #3진법 변환
    while n > 0 :
        n,m = divmod(n,3)
        answer += str(m)
    
    #10진법으로 변환
    return int(answer,3)
