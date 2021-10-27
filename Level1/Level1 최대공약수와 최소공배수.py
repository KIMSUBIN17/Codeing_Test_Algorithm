/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12940 */

def gcd(n,m):
    mod = m % n
    if mod != 0:
        m,n = n, mod
        return gcd(n,m)
    else:
        return n    

def solution(n, m):
    answer = [gcd(n,m), n*m / gcd(n,m)]
    return answer

'''
#풀이(다른사람 풀이 참고)
유클리드 호제법 이용
2개의 자연수 a,b에 대해서 a를 b로 나눈 나머지를 r이라 하면(a>b인 경우), a와 b의 최대공약수는 b와 r의 최대공약수와 같음

- GCD(최대공약수)
A,B가 주어지면 A,B를 서로 나누어서 0이 될 때까지 나머지를 구함
if A%B = 0, GCD = B
else GCD(B,A % B)

- LCM(최소공약수)
(A*B)/GCD



#다른 사람 풀이




--------------------
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]
입출력 예 설명
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.