# 좀 더 효율적인 풀이
#한턴의 정의 = 현재 가진 콜라를 전부 소진한다 !
def solution(a, b, n):
    answer = 0
    #1. 빈 병의 개수 n이 교환가능한 최소 숫자 a 이상일때까지 반복
    while n >= a:
        #2. newCount개의 병 추가
        newCount = n // a * b
        answer += newCount
        #남은 병 계산
        #n을 a로 나눈 나머지값만 남아있을 것이고, newCount갯수만큼을 더함(이번 턴에서는 newCount개수만큼 새로운 콜라를 받았다는의미)
        #a대신 a의 배수가 빠질 것
        n = n % a + newCount
    return answer



