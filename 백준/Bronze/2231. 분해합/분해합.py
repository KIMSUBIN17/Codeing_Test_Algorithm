import sys
input = sys.stdin.readline

#입력받은 값 정수로 변환( n : 우리가 찾으려는 분해합 값)
n = int(input())
# i를 0 ~ n-1 까지 반복(n이상의 값은 분해합이 될 수 없음)
for i in range(n):
    # i를 문자열로 변환하여 각 자릿수를 순회할 수 있도록
    # 문자열로 변환된 i의 각 자릿수를 정수로 변환 --> map(int, str(i))
    # i자신과 각 자릿수의 합을 더한 값이 분해합 
    digit_sum = i + sum(map(int,str(i)))
    #생성자일 경우
    if digit_sum == n : 
        print(i)
        break
# for 루프 다 돌때까지 break되지 않았다면 n의 생성자가 없으므로 0출력
else:
        print(0)


'''
# 참고자료_파이썬 각 자릿수 분리, 더하기 
https://go-hard.tistory.com/96

Q. 입력받은 숫자 n을 문자열로 변환하는 이유
A. 문자열로 변환하면 숫자의 각 자릿수가 독립된 문자로 분리되기 때문에, 반복문을 통해 직관적으로 코드화할 수 있음.
복잡한 수학연산없이 간단히 자릿수 접근 가능
def digit_sum(n):
    return sum(int(digit) for digit in str(n))


cf) 문자열 변환 없이 처리한다면? 몫과 나머지 연산 사용 
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10  # 마지막 자릿수를 더함
        n //= 10         # 마지막 자릿수를 제거
    return total
    
문자열 변환 없이 처리해야 하는 경우:
- 성능 최적화가 필요한 경우: 문자열 변환은 추가적인 메모리 사용과 변환 연산이 필요하므로, 속도가 중요할 때는 수학적 접근(몫과 나머지 방식)이 더 적합합니다.
- 제약 조건이 있을 경우: 문자열 변환이 금지된 문제라면 수학적 접근을 선택해야
'''
