def solution(numbers):
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for index, num in enumerate(nums):
        numbers = numbers.replace(num,str(index))
    return int(numbers)

'''
입력받은 numbers의 요소에서 num을 문자열 인덱스로 바꿔줌
마지막에 다시 int형으로 변환해 return
'''