def solution(before, after):
    answer = 0
    before = sorted(before)
    after = sorted(after)
    if before==after:
        return 1
    else:
        return 0
    
'''
순서 바꿔서 같은 단어가 되려면,
정렬했을때도 같은 값이 나와야 하기때문에 
각각의 문자열을 정렬해서 비교함

'''