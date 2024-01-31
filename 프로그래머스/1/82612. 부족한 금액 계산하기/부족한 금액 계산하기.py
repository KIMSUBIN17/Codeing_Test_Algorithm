def solution(price, money, count):
    cost = 0    #놀이기구를 count번 타기위해 내야하는 총 비용
    
    for i in range(1,count+1):
        cost += price * i   # count 변수에 비용 더해서 cost
        
    if cost > money : # 전체 비용 > 내가 가진 돈
            return cost - money # 비용 - 내가 가진 돈 
    else:   #금액 부족하지않으면
            return 0


''' # 이전 다른 풀이 
def solution(price, money, count):
    answer = -1
    
    answer = price * ((count)*(count+1)/2) - money
    if answer < 0:
        answer = 0
    return answer
'''