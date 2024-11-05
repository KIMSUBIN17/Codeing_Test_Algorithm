import sys
input = sys.stdin.readline

# 온라인 회원 수 N
n = int(input())

# 회원 정보 저장 리스트 생성
user = []

for _ in range(n):
    age, name = input().split()  # 나이와 이름을 공백으로 구분하여 입력
    user.append((int(age), name))  # 나이와 이름을 튜플로 묶어 리스트에 추가
    
# sort() 메서드를 사용하여 리스트 자체를 나이 기준으로 정렬
user.sort(key=lambda x: x[0]) 

# 정렬된 리스트를 출력
for age, name in user:
    print(age,name)
    