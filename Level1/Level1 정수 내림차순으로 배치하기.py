#링크 : https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = list(str(n))
    return int(''.join(sorted(list(answer), reverse = True)))

#입력받은 정수n을 str함수 사용해 문자열로 만들고 answer에 담음
#answer를 sorted함수와 reverse=True사용해 내림차순으로 정렬
#리스트값을 문자열로 변환하고 이를 int함수 사용해 정수로 반환

