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