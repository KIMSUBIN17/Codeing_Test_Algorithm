from collections import Counter

#입력 받기
numbers = []
for _ in range(10):
    numbers.append(int(input()))
    
#평균계산
avg = sum(numbers) // 10

#최빈값 계산
counter = Counter(numbers)    #각 숫자의 등장 빈도를 센다
mode = counter.most_common(1)[0][0]        #가장 많이 등장한  숫자 찾음
'''
most_common(1):등장 횟수가 가장 많은 숫자(최빈값)
most_common(1)[0][0]   --> 그 중 숫자만 가져옴
'''

print(avg)
print(mode)