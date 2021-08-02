# 링크 : https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    #최종결과출력_리스트를 문자열로 변환하여 출력
        return (''.join(sorted(list(s), reverse = True)))
    #내림차순 정렬
    #a.sort(reverse = True)
    #대문자는 소문자보다 ASCII 값이 작음 -> 대문자가 뒤로 감(내림차순)