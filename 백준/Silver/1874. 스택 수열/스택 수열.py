n = int(input())  # 수열의 크기
find = [int(input()) for _ in range(n)]  # 목표 수열 입력

stack = []  # 스택 선언
result = []  # 연산 기록
current = 1  # 스택에 push할 수 시작 숫자

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