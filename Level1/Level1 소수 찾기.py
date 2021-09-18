/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12921 */

def solution(n):
    n = n+1
    answer = [True]*n
    for i in range(2, int(n**0.5)+1):
        if answer[i] == True:
            for j in range(i+i,n,i):
                answer[j] = False
    a = [i for i in range(2,n) if answer[i]==True]
    
    return len(a)

'''
#문제
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

#제한 조건
n은 2이상 1000000이하의 자연수입니다.

#참고 풀이
1. 리스트 answer를 모두 소수라고 생각하고 True로 초기화
(인덱스n사용하기 위해 n=n+1로 설정)
2. 2부터 int(n**0.5)까지 소수인지 확인
3. 2번에서 소수인 숫자의 배수들은 소수가 아니므로 다음 for문에서 소수가 아니라고 False로 바꿔줌
4. 2,3번 반복
5. 리스트 answer의 값이 True(소수인 것) 값들의 개수를 리턴

#틀린풀이
def solution(n):
    count = 0
    
    for n in range(2, n+1):
        for i in range(2,n):
            if n%i == 0:
                break
            else:
                count+=1
    return count

->시간초과 발생(n을 2부터 n-1까지의 숫자들로 모두 나눔)
->해결법:sqrt(n) == n**0.5까지만 실행
->이유:n의 최대약수가 int(n**0.5)이하이기 때문

#해결법 : 에라토스테네스의 체 사용
현재 숫자들 중 가장 작은 수를 소수라 가정하고, 그 수의 배수를 모두 소수가 아니라고 체크하는 것 -> 최종적으로 소수들만 뽑아낼 수 있음
예시)
1. 1은 소수가 아니므로 2부터 확인
2. 현재 가장 작은 수:2 -> 2의 모든 배수 False 체크
3. 체크 안된 가장 작은 수:3 -> 3의 모든 배수 False 체크
4. 체크 안된 가장 작은 수:5 -> 5의 모든 배수 False 체크
5..... n에 도달할 때까지 반복
->에라토스테네스의 체 방식 사용안하면 통과X

#더 간단한 풀이_set 사용
def solution(n):
    num = set(range(2,n+1))
    print('num',num)
    
    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


1. 2부터 n까지 중복제거한 리스트 생성
2. 2부터 n까지 소수인지 확인하는 과정에서 소수인 숫자들은 set통해서 제거하여 num설정
3. 이 과정 반복
4. num의 길이를 리턴


'''