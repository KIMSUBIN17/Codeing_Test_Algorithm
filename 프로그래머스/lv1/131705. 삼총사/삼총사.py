# 전체 주어지는 수가 작아서 for문으로 구할 수 있었으나, 
# 수가 많아지면 n^3이 되므로 다른 방법을 찾아봐야할 것
def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

'''
1. 첫번째학생부터 ~ / 2. 첫번째 다음부터 / 3. 두번째 다음학생부터 ~
'''