def solution(s):
    stack = []
    
    for char in s:
        #스택이 비어있지 않고, 현재 들어온 문자가 스택 맨 위 문자와 같다면 짝을 이루어 제거됨
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # 스택에 현재 문자 추가
            stack.append(char)
    # 스택이 비어있으면 짝지어 제거 가능 -> 1
    # 그렇지않으면 -> 0
    return 1 if not stack else 0