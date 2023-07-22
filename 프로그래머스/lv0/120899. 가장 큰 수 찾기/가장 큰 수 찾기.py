def solution(array):
    return [max(array), array.index(max(array))]

'''
인덱스 -배열의 위치값
list에서 가장 큰수 찾기 : max()
list에서 가장 작은 수 찾기 : min()
list에서 특정 값의 index추출 : index()


#다른 풀이
def solution(array):
    answer = [0,0]
    answer[0] = max(array)
    #answer.append(max(array))
    answer[1] = answer.index(max(array))
    return answer
'''