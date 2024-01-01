def solution(my_string):
    #my_string의 각 인덱스 i에 대해 my_string[i:]형태로 접미사 생성해서 answer라는 리스트에 저장
    answer = [my_string[i:] for i in range(len(my_string))]
    #answer리스트를 sorted함수 사용해 사전순으로 정렬해 sorted_answer라는 새로운  리스트에 저장
    sorted_answer = sorted(answer)
    return sorted_answer