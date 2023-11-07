def check(x):
    binary = bin(x)
    one = binary.count('1') #1의 갯수 count하는 용도
    return one

def solution(n):
    answer = n
    num = check(n)
    while True:
        answer += 1
        if int(check(answer)) == num:
            return answer
    
    
'''
# 다시풀어보기 ! 
다른풀이 참고링크 : 
https://velog.io/@falling_star3/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%EB%8B%A4%EC%9D%8C-%ED%81%B0-%EC%88%AB%EC%9E%90
1. 주어진 값에 대해 이진법으로 변환 후 1의 갯수 카운트 하는 check 라는 함수 생성
2. n을 이진법 변환했을때 1의 갯수 세기
3. n보다 큰 수 answer에 +1을 반복해가면서 n의 이진법 변환 1의 갯수와 같으면 break 후 answer값 return 

'''
