def solution(number):
    #각 자리 숫자의 합을 저장할 변수 sum 선언
    sum = 0
    
    #number를 문자열로 변환한 뒤 각 자리의 숫자를 추출
    #sum을 구하기 위해 int형으로 바꿔서 합계 구함
    for num in str(number):
        sum += int(num)
     
    answer = sum % 9 
    return answer
    
'''
# 다른 풀이
def solution(number):
    return int(number) % 9
'''