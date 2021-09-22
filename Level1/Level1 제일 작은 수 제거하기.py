/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12935 */

def solution(arr):
    if len(arr)>1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

'''
#문제 설명
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

#제한 조건
arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

#풀이
1. 배열 arr은 길이 1이상이므로 if조건에 arr의 길이가 1보다 크다는 조건 부여
2. min()이용해 최솟값 구하고, remove로 배열 arr내에서 제거 후 배열arr을 리턴
3. else구문으로 배열이 빈 배열의 경우 배열에 -1 채워서 리턴하게끔 작성


'''