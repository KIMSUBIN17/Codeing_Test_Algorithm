def solution(array):
    return sorted(array)[len(array)//2]


'''
sorted사용해 정렬하여 중간 index의 값을 가져옴
중간index값은 배열 array의 길이를 2로 나눈 몫을 가져옴
//연산자 : 나머지 버리고 몫만 가져옴
'''