def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
        chicken = div + mod
    return answer


'''
# divmod() 사용해 좀 더 간결하게 표현하기 
>> divmod(a,b)를 이용하여 a를 b로 나눈 몫과 나머지를 한번에 변수에 저장할 수 있다. (단, 2개의 변수 선언 필요!)

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div+mod
    return answer
    

(참고링크 : https://velog.io/@jsanga214/%EC%BD%94%ED%85%8C%EC%A4%80%EB%B9%84-math)


'''