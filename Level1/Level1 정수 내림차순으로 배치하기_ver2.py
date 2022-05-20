/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12933 */

def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    
    return int("".join(n))

'''
1. 정수n을 str로 변환->list로 변환
2. list n을 sort()함수로 내림차순 정렬(reverse=True)
3. list->string으로 ""join()변환하고 int로 변환해 return
'''




'''
- sorted() : 리스트, 문자열 둘다 적용 간으 / 정렬결과 리턴 -> 변수에 담기 가능
- sort() : 리스트만 가능, SORT()로 문자열 정렬 시 ERROR발생
-> 리턴X.. 입력을 출력으로 덮어쓰기 때문에 별도의 추가 공간 필요X
 / 변수 담기 불가 --> 에러발생


'''
