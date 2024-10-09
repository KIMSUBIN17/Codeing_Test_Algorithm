N = int(input())  # N번 방 입력 받기

# 1번 방은 예외 처리
if N == 1:
    print(1)
else:
    layer = 1  # 첫 번째 층 (1번 방)
    count = 1  # 중앙에서부터 시작_현재 몇 번째 방까지 포함했는지 계산하는 변수(처음에는 1번방만 포함)
    
    # 반복문을 통해 몇 번째 층에 있는지 찾음
    # N번방이 포함될때까지 반복
    while N > count:
        count += 6 * layer  # 각 층에 추가되는 방의 수: 6 * layer
        layer += 1        # 층을 증가시킴 
        

    print(layer)