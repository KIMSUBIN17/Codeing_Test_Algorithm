def solution(numbers,num1,num2):
    return numbers[num1:num2+1]     #num1부터 num2+1까지

'''
인덱스 숫자로 list 슬라이스를 할 수 있음
list[start.index:end.index] --> start index에서 end.index 바로 앞까지 슬라이싱 가능
문제는 num2번째 인덱스까지 슬라이싱 --> end index+1이됨
'''