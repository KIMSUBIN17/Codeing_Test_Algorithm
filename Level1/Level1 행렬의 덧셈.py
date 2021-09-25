/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12950 */

def solution(arr1, arr2):
    answer = arr1

    for i in range(len(arr1)):  #행
        for j in range(len(arr1[i])):   #열
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer

'''
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]

#풀이
2차원 리스트 사용-->이부분 다시 공부해보기
for i in range(len(arr1)) : 두 배열의 길이가 같다고 가정하기 때문에 첫번째 배열의 길이만큼 반복
for j in range(len(arr1[i])) : 리스트의 첫번째 인덱스,두번째인덱스 -> 리스트 안에 리스트


#다른사람풀이
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A


#zip을 활용한 풀이!
zip은 동일한 개수로 이뤄진 iterable 한 자료형을 튜플로 묶어준다 ex) list(zip([1,2,3], [4,5,6])) -> [(1,4),(2,5),(3,6)]

def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    return answer

1. zip을 이용해 입력 받은 arr1과 arr2를 묶고 이를 for문을 통해 a,b로 할당.
2. a,b를 for문 활용해 c,d로 할당하고 이를 더한다음에 [ ] 를 활용해 list로 만들고 return

'''