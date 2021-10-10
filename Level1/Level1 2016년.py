/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12901 */

def solution(a, b):
    #2016년 1월 1일이 금요일부터 시작하기때문에 day 리스트의 시작을 FRI로 정함
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    #month리스트는 1월~12월까지의 일 수를 담은 리스트
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31] 
    
    #month배열의 a-1월까지 더한 수에 (3월이라면 2월까지의 날짜를 다 더한수)
    #구하고자하는 b날짜를 더하고 7로 나눈 나머지의 인덱스에 해당하는 수 return 
    return day[(sum(month[:a-1]) + b ) % 7]
'''
#풀이
- 요일은 7씩 반복되는 규칙을 가짐
- 매달 날짜는 다르므로 배열에 각각 저장(month리스트)
( 이 이후는 검색을 통해 다른 사람들의 풀이를 참고-> 리스트 [:n] 슬라이스, 인덱싱 활용법 연습의 필요느낌)


#다른 사람 풀이

def solution(a, b):
    answer = ''
    
    #2016년 1월 1일이 금요일부터 시작하기때문에 day 리스트의 시작을 FRI로 정함
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    #리스트를 반복하기 위해 곱함
    day = day*55
    #month리스트는 1월~12월까지의 일 수를 담은 리스트
    pattern = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    #2016년 a월 b일이 무슨 요일인지 찾기
    answer = day[sum(pattern[:a]) + b - 1 ]

-> a=3, b=25일이 주어졌다면? 일수로는 총 31+29+31+25이다.
FRI부터 시작하는 pattern리스트에서 인덱싱하면 원하는 요일값을 찾을 수 있다
-> 리스트에 대한 이해 필요(인덱싱)


2. datetime함수 사용(1)

import datetime 
def solution(a, b): 
    answer = '' 
    weekday_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"] 
    
    weekday_info = datetime.datetime(2016, a, b).weekday() 
    
    answer = weekday_list[weekday_info] 
    return answer


import datetime(2)

def solution(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

-> datetime객체는 년,월,일,시,분,초 필드 가지고 있고, 필요한 부분만 사용가능
weekday() : 요일 반환(0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
now() : 현재시각을 datetime.datetime클래스 객체로 반환


--------------------
문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
입출력 예
a	b	result
5	24	"TUE"
'''
