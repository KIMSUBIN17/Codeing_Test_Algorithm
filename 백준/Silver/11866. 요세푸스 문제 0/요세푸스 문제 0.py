from collections import deque

# 입력 처리
N, K = map(int, input().split())

# 1부터 N까지의 사람 리스트를 큐로 초기화
queue = deque(range(1, N + 1))
result = []

# 요세푸스 순열 생성
while queue:
    # K-1번 회전 후 K번째 사람 제거
    queue.rotate(-(K-1))
    result.append(queue.popleft())

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")


'''
# 문제풀이
# 큐 사용
- 사람들을 큐(리스트)로 초기화. 1번부터 N번까지의 사람을 순서대로 배치
- K번째 사람을 제거하고, 나머지 사람들로 계속 작업을 반복
# 순환 구현
- 큐에서 K-1번만큼 앞의 요소를 뒤로 이동시키는 방식으로 K번째 요소를 맨 앞으로 가져오고,
K번째 요소를 제거하고 이 과정 반복

    
'''
