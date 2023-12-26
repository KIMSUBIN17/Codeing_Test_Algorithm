def solution(myString):
    answer = myString.lower()
    #replace('a','A') --> a를 A로 변환
    answer = answer.replace('a','A')
    return answer


''' 아래 코드는 히든테스트케이스에서 오답처리됨
def solution(myString):
    answer = ''
    #myString문자열을 돌면서
    for char in myString:
        #a를 찾으면 A로 변환
        if char == 'a':
            answer += 'A'
        #대문자 알파벳은 소문자로 변환하여 새로운 문자열 answer에 추가
        elif char.isupper():
            answer += char.lower()
        else:
            answer+= char
    return answer

'''
