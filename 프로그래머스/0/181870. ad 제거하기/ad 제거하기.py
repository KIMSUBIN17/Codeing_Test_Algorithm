def solution(strArr):
    # 리스트컴프리헨션 사용 -> ad를 포함하지 않는 문자열들을 새로운 리스트에 선택하여 반환
    answer = [s for s in strArr if "ad" not in s]
    return answer

'''
* for문에서 strArr대신에 len(strArr) 작성했을때 오류 발생
>> TypeError: 'int' object is not iterable (정수 자체는 반복할 수 없다)
정수형(int)변수를 for문에서 반복하려고 시도할때 발생하는 에러
정수형 변수는 iterable하지 않기 때문에 반복할 수 없음
- len(strArr)값을 구하려할때, 리스트가 아니라면 함수의 적용이 불가능하기 때문

iterable 객체 - 리스트(list), 튜플(tuple), 딕셔너리(dict), 집합(set), 문자열(str), range(범위값)
'''