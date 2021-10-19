/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12910 */

def solution(arr, divisor):
    answer = []
    
    #arr에 있는 자연수들을 하나씩 반복(array의 각 element들)
    for num in arr:
        #현재 숫자가 divisor로 나누어 떨어지면
        if num % divisor == 0:
            #answer에 현재 숫자를 넣음
            answer.append(num)
    
    #answer가 빈 리스트라면?
    if answer == []:
        #answer를 -1 하나가 담긴 리스트로 만듦
        answer = [-1]
    #answer가 빈 리스트가 아니라면?
    else:
        #answr의 값들을 오름차순으로 정렬
        answer.sort()
        
    return answer

'''
#풀이
1. array의 각 element들을 for문으로 돌림
1-1. 현재 숫자가 divisor로 나누어 떨어지면, answer 리스트에 저장
2. divisor로 나누어 떨어지는 element가 하나도 없으면(answer가 빈 리스트라면 answer에 -1하나가 담긴 리스트로 만듦
2-1. answer가 빈 리스트가 아니라면, answer의 값들을 오름차순으로 정렬
3. answer리스트 반환



--------------------

문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
입출력 예
arr	divisor	return
[5, 9, 7, 10]	5	[5, 10]
[2, 36, 1, 3]	1	[1, 2, 3, 36]
[3,2,6]	10	[-1]
입출력 예 설명
입출력 예#1
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

입출력 예#2
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

입출력 예#3
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

'''
