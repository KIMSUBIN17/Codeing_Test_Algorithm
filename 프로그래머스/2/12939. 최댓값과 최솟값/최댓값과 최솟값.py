def solution(s):
    answer = ''
    #s에는 둘 이상의 정수가 공백으로 구분되어 있음
    #문자열로 나열된 숫자들은 int형으로 변환해주고 이를 list에 담음
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))


'''
다른풀이
def solution(s):
    answer = ''
    # s에는 둘 이상의 정수가 공백으로 구분되어 있다
    nums = s.split()
    new_nums = []
    for num in nums:
        new_nums.append(int(num))
    answer += '{0} {1}'.format(min(new_nums), max(new_nums))
    return answer
'''
