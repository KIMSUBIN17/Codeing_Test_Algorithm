def solution(rsp):
    result = {'2':'0','0':'5','5':'2'}
    answer = ''
    for i in rsp:
        answer += result.get(i)
    return answer

'''
딕셔너리 만든 후 get()사용해 value값 찾음
더 짧은 풀이ver
def solution(rsp):
    result = {'2':'0','0':'5','5':'2'}
    return ''.join([result.get(i) for i in rsp])
'''