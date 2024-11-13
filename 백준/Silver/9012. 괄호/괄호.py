T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:  #스택에 괄호가 없으면 no출력
                print("NO")
                break
    else:  #break문 타지않고 수행됐을 때
        if not stack: 
            print("YES")
        else: #스택안에 괄호가 남아있다면 짝이 맞지 않는 것
            print("NO")