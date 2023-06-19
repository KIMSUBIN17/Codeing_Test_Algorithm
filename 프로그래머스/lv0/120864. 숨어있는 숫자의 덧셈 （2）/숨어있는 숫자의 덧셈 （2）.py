def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i,' ')
    my_string = my_string.split()
    return sum(list(map(int, my_string)))    




'''
isalpha() : 대소문자 관계없이 알파벳인지 판별
replace()사용해 알파벳이면 그 자리를 공백(' ')으로 바꾸고 전체 문자열my_string을 공백 기준으로 split하여 문자열에서 숫자만 남김
sum을 구하기 위해 숫자만 남은 문자열을 int형으로 바꾼 뒤 sum사용해 전체 합 구함
'''

#다른풀이:re라이브러리 + 정규표현식 사용

'''
import re

def solution(my_string):
    num = re.findall(r'\d+', my_string)
    num = list(ma[(int, num)])
    retur sum(num)

문자열의 길이가 길어지면 for문의 연산속도도 함께 길어짐
--> 정규표현식 사용
re라이브러리-findall() : 주어진 패턴에 해당하는 내용들만 리스트로 만들어줌

연속되는 숫자 34도 3,4가 아닌 34 하나의 수로 인식하기 위해서 1번 이상 반복되는 정수를 의미하는 r'\d+'를 패턴으로 작성함
마지막에는 문자열인 숫자를 정수형으로 변환한 뒤 sum으로 전체 합계 구함

# 참고 링크 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%A8%EC%96%B4%EC%9E%88%EB%8A%94-%EC%88%AB%EC%9E%90%EC%9D%98-%EB%8D%A7%EC%85%882-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
'''