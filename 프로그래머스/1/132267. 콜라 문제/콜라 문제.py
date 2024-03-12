#단순 구현
def solution(a, b, n):
    answer = 0
    #1. 빈 병의 개수 n이 교환가능한 최소 숫자 a 이상일때까지 반복
    while n >= a:
        #2. b개의 병 추가
        # a개 먹고 b개만큼 새로 받음
        answer += b
        #남은 병 계산
        #n에서 a개 쓰고 b개를 새로 받았음
        n = n - a + b
    return answer


'''
참고링크
https://coding-grandpa.tistory.com/113
https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%BD%9C%EB%9D%BC-%EB%AC%B8%EC%A0%9C-Python

1. 단순 구현 문제
--> 비효율적이지만 정답을 만들 수 있는 코드를 만드는 연습중요


'''