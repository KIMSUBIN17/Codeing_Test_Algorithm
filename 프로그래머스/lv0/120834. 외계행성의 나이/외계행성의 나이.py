def solution(age):
    answer = '' #저장공간
    for i in str(age):  #str로 한글자씩 
        answer += chr(ord(i)+49)
    return answer

'''
str로 안바꾸면 그냥숫자로 입력이 되어서 출력x
아스키코드표 참고
아스키코드(48:0)에 49를 더하면 아스키코드(97:a)이 나옴
str() : 정수,실수 -> 문자열
ord() : 문자열 -> 아스키코드로
ord('a') -> 97
chr() : 아스키코드 -> 문자열
나이를 str형으로 바꿈

#다른풀이 - 유튜브 참고
def solution(age):
    li = ['a','b','c','d','e','f','g','h','j']
    
    a = ''  # 저장공간
    for i in str(age): # 한글자씩 '5''1'  '2''3'
        a+=li[int(i)]  
        #5번지값,  1번지값 가져오려면-->li[i]
        #i값은 문자X 숫자니까 int(i)로 변환
    return a
'''