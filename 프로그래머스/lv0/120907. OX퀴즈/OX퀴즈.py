def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer


'''
# 다시풀어보기 !!!

# 오답 체크 
eval() 함수는 데이터 타입이 정수값으로 리턴되기 때문에 eval()과 비교시 int로 형변환 필요
'''