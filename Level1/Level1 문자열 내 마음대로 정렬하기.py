/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12915 */

def solution(strings, n):
    answer = []
    new = []
    
    for i in strings:
        new.append(i[n]+i)
    new.sort()
    
    for i in new:
        answer.append(i[1:])
    
    return answer
    

'''
#풀이
->문자열로 구성된 리스트 strings, 정렬 기준이 될 정수 n이 매개변수로 주어짐
1. n번을 인덱싱하기 위해 for문에서 new라는 새로운 배열에 요소를 append함
2. 각 문자열의 n번째 글자를 기준으로 오름차순해야하므로 sort로 정렬
3. 리턴해야할 answer에서 new리스트의 맨 앞자리만 제거하도록 슬라이싱함

# sorted
sort()와 차이점: sort() 메서드는 리스트에서만 정의가 됨. 이와 달리 sorted() 함수는 모든 이터러블(파이썬에서 반복문을 사용할 수 있는 객체)을 받아들임

sorted()는 각 리스트 요소에 대해 호출할 함수를 지정하는 key매개 변수를 가지고 있다.

->sort함수와 lambda식 사용에 익숙해지기
lambda식 사용 장점 : 코드의 간결함, 메모리 절약
lambda 인자 : 표현식
# 예시

def plus(x, y):
	return x + y
plus(1, 2)  # 값: 3

# 위의 함수를 람다로 표현한다면?
(lambda x,y: x + y)(1,2)  #값: 3

문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
입출력 예
strings	n	return
["sun", "bed", "car"]	1	["car", "bed", "sun"]
["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]
입출력 예 설명
입출력 예 1
"sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다. 이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] 입니다.

입출력 예 2
"abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다. 따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다. "abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 답은 ["abcd", "abce", "cdx"] 입니다.



#다른사람풀이

1. lambda식 사용
#문자열로 구성된 리스트 strings, 정렬 기준이 될 정수 n이 매개변수로 주어짐
def solution(strings,n):
    #string에 있는 문자열들을 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
    #인덱스 n번째의 문자가 같은 문자열이 여럿일 경우 사전순으로 정렬
    #결과는 answer변수에 저장
    
    answer = sorted(strings, key = lambda string: (string[n], string))
    #answer에 저장되어있는 정렬이 된 문자열 리스트 반환
    return answer


'''