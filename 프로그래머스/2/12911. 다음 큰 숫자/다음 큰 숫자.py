def solution(n):
    next = n
    answer = 0
    while True:
        next += 1
        if bin(n)[2:].count('1') == bin(next)[2:].count('1'):
            answer = next
            break
    
    return answer
    
    
'''
# 다시풀어보기 ! 
1. 다른풀이 참고링크 : https://hoons-dev.tistory.com/16
브루트포스 (완전탐색)문제
1. 다음 숫자를 1씩 늘려가면서, 
2. 이진수 변환했을때 1의 갯수가 처음 수인 n과 같은지 비교하고 같으면 break 후 리턴


'''