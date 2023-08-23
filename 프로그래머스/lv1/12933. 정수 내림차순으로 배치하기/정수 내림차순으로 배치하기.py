def solution(n):
    # 1. 정수->문자열 / 2. 문자열 ->리스트 변환
    li = list(str(n))   
    #li 내림차순으로 정렬
    li.sort(reverse = True)
    return int("".join(li))

# sort() 문자열 정렬 시 error 발생
