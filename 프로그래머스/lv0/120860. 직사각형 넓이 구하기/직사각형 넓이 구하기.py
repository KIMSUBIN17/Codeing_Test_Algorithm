def solution(dots):
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    area = w*h
    return area


'''
w 리스트에 x값 좌표들을 넣고, h 리스트에 y값 좌표들을 넣고 
가로길이 = w 리스트의 최대값-w리스트의 최소값
세로길이 = h리스트의 최댓값 - h리스트의 최소값
'''
    