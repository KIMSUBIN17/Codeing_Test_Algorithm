def solution(n, lost, reserve):
    answer = 0


    #중복이 있을 수 있으므로 각 리스트를 set사용해서 중복된 번호 제거
    #도난당한 학생들의 번호
    set_lost = set(lost) - set(reserve)
    #여벌의 체육복을 가진 학생들 중 도난당한 학생들의 번호 제외 
    set_reserve = set(reserve) - set(lost)
    
    #여분의 체육복이 있는 사람을 기준으로 반복 
    for r in set_reserve:
        #최대로 많은 학생들에게 체육복을 빌려주기 위해 i-1번째 먼저 체크
        #i-1번째가 도난당한 사람이면 옷을 빌려줄 수 있음
        #set_lost에서 i-1제거
        if r - 1 in set_lost: 
            set_lost.remove(r-1)
        # 위 if문 조건 충족하지않고, i+1이 set_lost에 존재할 때
        elif r+1 in set_lost:   
            set_lost.remove(r+1)
    
    #최종적으로 set_lost에는 옷을 빌리지 못한 학생만 존재
    #set_lost를 제외한 나머지는 체육복을 입을 수 있음
    #전체학생수(n) - 체육복을 도난당한 학생들(set_lost) = 체육복을 가진 학생
    answer = n-len(set_lost)
    
    return answer
          
          
          
'''
#오답노트
- 문제에서 여벌의 체육복을 가져온 학생이 도난을 당한 경우도 있다고 했으므로 lost와 reserve의 중복을 제거
(차집합을 이용해 공통원소를 제거)
- 최대로 많은 학생들에게 체육복을 빌려주려면 i-1번째에 위치한 학생에게 옷을 빌려주는것을 우선적으로 고려해야함 
set_lost = set(lost) - set(reserve)
set_reserve = set(reserve) - set(lost)

n = 전체학생수 / set_lost:체육복을 도난당한 학생수

'''