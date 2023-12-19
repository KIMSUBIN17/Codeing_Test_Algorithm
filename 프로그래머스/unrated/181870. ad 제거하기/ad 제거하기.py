def solution(strArr):
    # 리스트컴프리헨션 사용 -> ad를 포함하지 않는 문자열들을 새로운 리스트에 선택하여 반환
    answer = [s for s in strArr if "ad" not in s]
    return answer