def solution(d, budget):
    answer = 0
    d.sort()
    #print(d)   오름차정렬
    for i in range(len(d)):
        #가장 작은 금액 신청한 부서부터 예산가능한 범위에서 지원하고, 지원해준만큼 예산에서 빼서 잔여예산을 가지고 반복
        if d[i] <= budget:
            #지원해줄수있는 부서의 수 answer에 +1
            answer += 1
            budget -= d[i]
        else:
            break
    return answer