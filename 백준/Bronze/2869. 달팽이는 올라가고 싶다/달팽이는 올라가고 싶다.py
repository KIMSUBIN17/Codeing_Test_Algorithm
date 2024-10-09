import math

# A, B, V 입력받기
A, B, V = map(int, input().split())

# 달팽이가 정상에 도달하는데 걸리는 일수 계산
# V-B : 마지막날 도달하기 직전까지 남은 높이
# A-B : 하루에 실제로 올라가는 높이
days = math.ceil((V - B) / (A - B))
#math.ceil():계산된값을 올림해서 정수로 만듦


print(days)