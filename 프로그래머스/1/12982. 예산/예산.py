def solution(d, budget):
    answer = 0
    d.sort()
    #print(d)
 #최대한 많은 부서를 지원하기 위해 -> 예산이 적은 팀 먼저 지원 
    #d를 돌면서 budget에서 빼줌
    for i in d:
        budget -= i
        #budget이 0보다 작으면, 예산소진이므로 for문 종료
        if budget < 0:
            break
        else:   #budget이 남아있으면 해당 팀을 지원할 수 있으므로 +1
            answer += 1
    return answer

'''
#pop을 사용한 다른 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

--> d를 정렬하고 신청한 지원금의 합이 예산보다 작아질때까지 while문돌다가 마지막 원소를 pop
--> 지원받는 부서는 남은 d의 개수를 구하면 됨=len(d)리턴

'''