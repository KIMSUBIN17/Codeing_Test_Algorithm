#링크 : https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = sorted(list(str(n)))
    return int(''.join(sorted(list(answer), reverse = True)))

#1. 입력 받은 정수 n을 str() 함수 사용해 문자열로 만듦-> list() 함수 사용해 리스트생성
#2. 만들어진 리스트를 sorted 함수에 넣고, reverse = True(내림차순)으로 정렬
#3. 리스트를 answer에 담고, ''.join(answer) 사용해 문자열 answer 리스트의 값을 문자열로 변환해 출력
#4. 변환된 문자열을 int()함수 사용해 정수로 반환
