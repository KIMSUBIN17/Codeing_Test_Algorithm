def solution(myString):
    result = ''
    #문자열 myString을 한글자씩 순회하면서
    for char in myString:
        #l보다 앞서는 문자라면 l로 변환
        if char < 'l':
            result += 'l'
        #아니면 그대로 둔다
        else:
            result += char
    return result


'''
def solution(myString):
    result = ''.join('l' if char < 'l' else char for char in myString)
    return result
'''