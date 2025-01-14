# 목표수열을 만들기 위해 수열의 크기 n을 입력받고, 
# n만큼 반복해서 사용자가 입력하는 숫자를 정수로 변환해 find 리스트에 저장하는 리스트컴프리헨션
# n번 반복에서 입력된 값을 정수로 변환하여 [] 로 변환된 값을 리스트에 담음
n = int(input())  # 수열의 크기
find = [int(input()) for _ in range(n)]  # 목표 수열 입력

stack = []  # 수를 담을 스택
result = []  # 연산 기록을 저장할 리스트 선언 
current = 1  # 현재 스택에 push할 숫자를 추적

for target in find:
    # target에 도달할 때까지 push
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 top이 target과 같다면 pop해서 꺼냄
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        # 스택의 top이 target과 다르다면 수열을 만들 수 없음
        print("NO")
        break
else:
    # 모든 연산 기록 출력
    print('\n'.join(result))





'''
💦 오답노트
- 시간 복잡도 : O(n) 
>> 각 숫자는 스택에 한번 push되고 한번 pop됨
# n만큼 반복해서 사용자가 입력하는 숫자를 정수로 변환해 find 리스트에 저장하는 리스트컴프리헨션
# n번 반복에서 입력된 값을 정수로 변환하여 [] 로 변환된 값을 리스트에 담음
n = int(input())  # 수열의 크기
find = [int(input()) for _ in range(n)]  # 목표 수열 입력
>> 이러한 방식은 입력 갯수가 고정된 경우에 편리함
sequence = []
for _ in range(n):
    sequence.append(int(input()))
위 for문과 동일동작을 한다고 생각하면 됨 

🧵 입력된 수열 처리
- 입력된 수열을 순서대로 처리하며, 원하는 숫자(target)이 될 때까지 스택에 push
- 스택의 top이 target과 일치하면 pop
- 스택이 top이 target과 일치하지 않고, 더이상 push 불가하다면 수열을 만들 수 없으므로 NO 출력
'''
