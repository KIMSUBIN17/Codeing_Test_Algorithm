/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12947 */

def solution(x):
    num = x
    sum = 0
    
    x = list(str(x))
    
    for n in x:
        sum += int(n)
    return num % sum == 0

'''
#풀이
1. 입력받은 자연수 x를 각 자릿수로 배열로 만들어 다 더함
2. x의 원래값과 더한 값을 모듈러 연산하여 나누어 떨어지면(0이 나오면) true 리턴


문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
입출력 예
arr	return
10	true
12	true
11	false
13	false
입출력 예 설명
입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.

#다른 사람 풀이
ver.간단
def solution(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

def solution(n):
    # n은 하샤드 수 인가요?
    s=sum([int(i) for i in str(n)])
    if n%s == 0:
        return True
    return False




'''