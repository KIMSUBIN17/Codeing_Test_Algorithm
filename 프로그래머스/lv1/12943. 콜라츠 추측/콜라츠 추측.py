def solution(num):
    count = 0	# 계산을 한 횟수를 저장하는 변수
    
    if num == 1:	# 최초의 num이 1 --> 0
        return 0
    
    while num != 1:	# num이 1이 아닐때까지만 반복
        if num % 2 == 0:	# num이 짝수
            num //= 2	# num을 2로 나눈다
        else:	# num이 홀수
            num = num * 3 + 1	
        count += 1	# 계산횟수 추가
        
        if count == 500:	# 계산횟수가 500번을 넘으면 종료
            return -1
    
    return count 



'''
def solution(num):
    answer = 0
    
    while (1):
        if num == 1 :
            break
        elif answer == 500 and num!= 1:
            answer = -1
            break

        if num % 2 == 0:
            num = num/2
        elif num % 2 == 1:
            num = num * 3 + 1
                    
        answer += 1

    return answer
'''

