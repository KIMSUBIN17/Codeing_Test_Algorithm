def solution(myString, pat):
    #A->X로 대체, B->A로 대체, X를 B로 대체하여
    #A->B, B->A로 변환한 후 
    #'pat'값이 이 문자열에 포함되어 있는지 확인하여 결과값을 반환
    if pat in myString.replace('A','X').replace('B','A').replace('X','B'):
        return 1
    else:
        return 0