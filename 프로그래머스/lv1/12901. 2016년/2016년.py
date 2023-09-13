'''
def solution(a, b):
    answer = ''
    
    #2016년 1월 1일이 금요일부터 시작하기때문에 day 리스트의 시작을 FRI로 정함
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = day*55
    #month리스트는 1월~12월까지의 일 수를 담은 리스트
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    #2016년 a월 b일이 무슨 요일인지 찾기
    answer = day[sum(month[:a]) + b - 1 ]


'''
def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31] 
    
    return day[(sum(month[:a-1]) + b ) % 7]