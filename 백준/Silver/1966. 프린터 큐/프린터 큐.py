# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 입력받기
    N, M = map(int, input().split())  # 문서 개수와 목표 문서의 인덱스
    prior = list(map(int, input().split()))  # 문서들의 중요도
    
    # 큐 생성: (중요도, 인덱스) 형태로 저장
    queue = [(prior[i], i) for i in range(N)]
    cnt = 0  # 인쇄 순서를 기록할 변수

    while queue:
        # 큐의 첫 번째 문서의 중요도가 가장 큰지 확인
        current = queue.pop(0)
        if any(current[0] < q[0] for q in queue):
            # 현재 문서보다 높은 중요도가 존재하면 뒤로 보냄
            queue.append(current)
        else:
            # 현재 문서를 인쇄
            cnt += 1
            if current[1] == M:
                # 목표 문서라면 결과 출력
                print(cnt)
                break