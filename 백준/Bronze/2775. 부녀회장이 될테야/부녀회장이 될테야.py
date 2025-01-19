t = int(input())        #테스트 케이스 개수 입력

for i in range(t):        #테스트 케이스 횟수만큼 반복
    k = int(input())        # 층
    n = int(input())        # 호
    
    # 0층의 각 호에는 호수 번호만큼이나 거주하므로 0층을 리스트로 초기화
    people = [i for i in range(1,n+1)]    #0층 초기화
    
    for x in range(k):        #k층까지 반복
        #현재 층의 각호에 사는 거주민 수를 계산한 값을 저장하는 리스트
        #k층 계산할 때, (k-1)층의 데이터를 이용해 만들어짐
        #계산이 완료되면 new값을 people로 복사하여 다음 층 계산에 사용
        new = []        
        for y in range(n):        #각 호수별로 계산
            new.append(sum(people[:y+1]))        #아래층의 1~y호까지의 sum
        people = new.copy()        #새로 계산된 층별 거주민 수 결과를 현재 층의 값으로 업데이트
        
    print(people[-1])        #마지막 값 출력(k층 n호의 거주민 수)
        