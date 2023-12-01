def solution(n):
    count = 0
    
    #두개의 반복문을 통해 연속된 자연수의 합을 계산
    #i를 1부터 n까지 반복하면서
    for i in range(1,n+1):
        total = 0
        
        # i부터 n까지의 합 계산
        for j in range(i,n+i):
            total += j
            
            #합이 n과 일치하면 count를 1증가
            if total == n:
                count += 1
                break
            #합이 n을 초과하면 stop
            elif total > n:
                break
    return count