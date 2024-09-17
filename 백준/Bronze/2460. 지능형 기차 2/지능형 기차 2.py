# 처음 기차에는 아무도 없으므로 사람 수를 0으로 저장해 시작
max_p = 0        #기차 안에 사람이 가장 많을 때의 사람 수 
current_p = 0        #현재 기차 안의 사람  수 


#10개 역에 대해 내린 사람과 탄 사람의 수 입력받음
for _ in range(10):
    off, on = map(int,input().split())    #내린 사람 수(off),탄 사람 수 (on)
    current_p -= off     #내린 사람만큼 현재 사람 수 감소
    current_p += on      #탄 사람만큼 현재 사람 수 증가
    
    #매 역마다 기차 내 사람 수를 계산하여 가장  큰 값을 저장
    max_p = max(max_p,current_p)
    
print(max_p)