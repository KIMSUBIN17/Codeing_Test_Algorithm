def solution(array, n):
    li = []
    answer = 0
    array.sort()

    for i in array:
        li.append(abs(i-n))
        
    return array[li.index(min(li))]



'''
1. array 정렬(마지막에 최소값의 인덱스 가져오기 위해)
2. for문 반복해 배열 array에 있는 값과 정수 n과의 차이를 구함(처음에 만든 li에 append) 
3. 절대값함수 abs()사용해 array요소와 n값의 차이를 구함
4. 마지막 array에서 index()함수 이용해 차이값 가장 작은 인덱스 리턴 

'''