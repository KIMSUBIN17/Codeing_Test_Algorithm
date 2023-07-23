def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

'''
# 다른 풀이
--> 배열의 원소중에서 최댓값 뽑아서 곱하기
def solution(numbers):  #[0,31,24,10,1,9] 정렬안된상태
    numbers.sort()      #오름차순
    return numbers[-1]*numbers[-2]
    
    


'''