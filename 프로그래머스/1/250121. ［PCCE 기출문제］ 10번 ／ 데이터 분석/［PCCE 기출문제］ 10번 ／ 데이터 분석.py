def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code": 0, "date": 1, "maximum":2, "remain": 3}
    
    #데이터필터링
    #dict[ext]통해 ext문자열에 해당하는 데이터 리스트의 인덱스를 찾고, d[dict[ext]]통해 value에 저장
    for d in data:
        value = d[dict[ext]]
        if value <= val_ext:
            answer.append(d)
    #데이터정렬_answer리스트를 sort_by기준으로 정렬
    answer.sort(key = lambda x: x[dict[sort_by]])
    return answer


'''
각 필드는 특정 의미를 가지고, 이를 기준으로 필터링 및 정렬 해야함
문자열로 주어진 기준을 데이터 리스트의 특정 인덱스와 매핑해야함
* 딕셔너리를 사용하는 이유 
- 빠른 조회
문자열 기준(ext, sort_by)을 데이터 항목의 인덱스로 변환하는 작업이 필요. 딕셔너리 사용하면 문자열 기준을 인덱스로 변환하는 작업이 빠름
(ex. "data"문자열 --> 1로 변환이 빠름)
- 코드의 가독성 및 유지보수성
각 문자열 기준이 어떤 인덱스를 의미하는지 파악 쉬움
데이터 형식이 변경되거나 추가 기준이 생기면, 딕셔너리만 업데이트 하면 됨(코드수정할 필요 x)
- 일관된 접근방식
문자열 기준을 인덱스로 변환하는 과정을 일관되게 처리할 수 있음 

'''