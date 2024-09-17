n = int(input())
answer = 'int'
for i in range(n//4):
    answer = 'long ' + answer
print(answer)


'''
입력값을 4로 나눈 몫만큼 반복하여 'long'문자열을 붙여줌
'''