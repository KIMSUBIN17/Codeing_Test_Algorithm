
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count=0     #약수의 개수 담을변수
        
        for j in range(1,i+1):
            if i % j == 0:
                count += 1      #약수개수
        if count % 2 == 0:  #약수개수가 짝수
            answer += i
        else:   #약수개수가 홀수
            answer -= i
    
    return answer