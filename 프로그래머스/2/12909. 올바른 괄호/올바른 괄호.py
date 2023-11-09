def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append('(')
        else:  # i == ')'인 경우
            # 스택이 빈 경우 ')'가 들어올 때
            if stack == []:  
                return False
            else:
                # 스택안에 '('가 있는 상태에서 ')'가 들어와 짝을 이루면 올바른 괄호 완성 -> 스택에서 제거
                stack.pop()  
    
    #for문 종료 이후 '(' 가 남아있다면
    if stack != []:
        return False
    
    return True



'''
생각한 방법:
stack 자료형에서 append,pop
'()' 짝이 되어야 올바른 괄호로 
스택에는 '(' 만 넣고, ')'이 들어올 때에만 삭제
스택이 비어있는데 ')'가 들어오면 올바른 괄호가 될 수 없음 -> False
for문 다 돌았는데 stack안에 '('가 남아있으면 올바른 괄호 아님 -> False


스택큐로 방향을 바꿔서 '('일 경우 리스트에 append, ')'일경우 pop. 
만약 리스트가 비었는데 '('가 한 번 더 나와서 오류가 발생했다면, return False하도록 함
'()'로 완전히 괄호가 완성됐을 때 ')'가 이어지면 닫을 수 없는 괄호라 False이기 때문이다.
리스트 안이 다 비어지면 True 아니면 False


참고링크 : https://velog.io/@ssongplay/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%98%AC%EB%B0%94%EB%A5%B8-%EA%B4%84%ED%98%B8-Python

https://velog.io/@falling_star3/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%EC%98%AC%EB%B0%94%EB%A5%B8-%EA%B4%84%ED%98%B8
'''