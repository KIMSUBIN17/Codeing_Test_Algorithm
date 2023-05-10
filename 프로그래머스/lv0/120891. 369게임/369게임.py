def solution(order):
    answer = 0
    for i in str(order):
        if i in ["3","6","9"]:
            answer += 1
    return answer



'''
첫번째 for 문 : 말해야하는 숫자 order 를 문자열로 변환
두번째 for 문 : 3 6 9숫자가 있으면 answer 값을 +1함 


# 다른 사람 풀이 
def solution(order):
    answer = str(order).count("3") + str(order).count("6") + str(order).count("9")
    
    return answer

--> str()을 사용해 문자열로 변환 / 
count()함수 사용해 3 6 9 갯수 count
'''