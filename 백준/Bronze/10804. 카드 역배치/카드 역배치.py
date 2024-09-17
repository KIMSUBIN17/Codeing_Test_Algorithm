# 초기 카드 배열
cards = list(range(1, 21))

# 10개의 구간을 입력 받기
for _ in range(10):
    a, b = map(int, input().split())
    # 슬라이싱을 이용한 부분 배열의 뒤집기
    cards[a-1:b] = cards[a-1:b][::-1]

# 결과 출력
print(" ".join(map(str, cards)))
