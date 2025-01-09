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
# 큐 사용 / deque의 rotate메서드 사용
- 요세푸스 문제에서는 K -번째 사람을 제거하고 그 사람부터 다시 카운트를 시작함
    --> 원형 구조를 반복적으로 구현해야함을 의미(포인트)
- 사람들을 큐(리스트)로 초기화. 1번부터 N번까지의 사람을 순서대로 배치
- K번째 사람을 제거하고, 나머지 사람들로 계속 작업을 반복
# 순환 구현
- 큐에서 K-1번만큼 앞의 요소를 뒤로 이동시키는 방식으로 K번째 요소를 맨 앞으로 가져오고,
K번째 요소를 제거하고 이 과정 반복


# 왜 K - 1번째를 사용하는가
- K번째사람을 제거하는 것 = 큐의 맨 앞의 요소를 기준으로 K-1개의 요소를 뒤로 보낸 후, 
K번째 요소를 제거해야함
    --> 큐의 맨 앞 요소를 K-1번 뒤로 보내면, K-번째 요소가 큐의 맨 앞에 위치하게되고, 이를 pop해서 처리가능
- K-1번 회전하면 K번째 사람이 큐의 맨 앞에 있게 되고, 맨 앞 요소를 제거하면 K번째 사람을 제거하는 것과 같은 효과가 되므로 (******)
- n=7, k=3 예시로 볼때, k-1를 2번 회전하게 되면, 
1 2 3 4 5 6 7 에서 앞의 두 요소 1,2가 맨 뒤로 가게 되어,
K번째 요소인 3이 맨 앞으로 오게된다. 이때 맨앞 요소 3을 pop하게 되면 K번째 요소를 제거하는 것과 동일한 로직임
- (K-1) : K-1개의 요소를 큐의 뒤로 보내 K번째 요소가 맨 앞으로 오도록. 
- K-1이 음수인 이유는 음수로 rotate 사용 시 왼쪽으로 회전하기 때문에

    
'''
