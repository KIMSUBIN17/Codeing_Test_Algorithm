import sys
input = sys.stdin.readline

# 입력
ans = 0        # 다음 출력될 값(숫자)을 저장하는 역할

for i in [3, 2, 1]:        
    tmp = input().rstrip()
    #입력값tmp가 아래중 하나가 아니면 숫자, 숫자인경우 ans값을 계산해 업데이트
    if tmp not in ['Fizz', 'Buzz', 'FizzBuzz']:
        ans = int(tmp) + i

# 출력
if ans%3 == 0 and ans%5 == 0:
    print('FizzBuzz')
elif ans%3 == 0:
    print('Fizz')
elif ans%5 == 0:
    print('Buzz')
else:
    print(ans)

''' #오답노트 _ 다시풀어보
for i in [3, 2, 1]:
# 3,2,1리스트를 순회하며 첫번째입력값->3을 더함, 두번째 입력값-> 2를 더함 / 세번째 입력값 -> 1을 더함
# 입력값이 FizzBuzz의 연속된 3개의 값이므로, 마지막 값에 1을 더하면 다음 값이 됨

if tmp not in ['Fizz', 'Buzz', 'FizzBuzz']:
    ans = int(tmp) + i
-> 여기서 i는 [3, 2, 1] 순으로 들어가므로, 가장 마지막 숫자에 1을 더해 다음 숫자를 구하는 원리

입력값을 뒤에서부터 숫자를 찾고, 해당 숫자에 1을 더해 다음 값을 구하는 방식
ans 값을 찾은 후, FizzBuzz 규칙을 적용하여 출력
'''
