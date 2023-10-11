def solution(name, yearning, photo):
    answer = []
    # 결과값선언, 이름과 그리움 점수는 길이가 같다는 조건을 활용해 zip()을 이용해 info라는 딕셔너리를 생성
    info = dict(zip(name, yearning))
    for people in photo:
        #사진별로 사람들의 그리움 점수를 담기위한 변수 score
        score = 0
        #for문 돌면서 사진 속 사람들 각각의 점수 누적
        for person in people:
            score += info.get(person,0)
        answer.append(score)
    return answer


'''
#풀이참고 
https://aiday.tistory.com/133
길이가 같은 리스트들의 요소들을 차례대로 조합해서 새로운 리스트, 딕셔너리로 만들어야함
-> zip()
리스트명을 zip()안에 순서대로 넣음
그냥 zip()만 사용하면 리스트의 내용물이 분배된 상태로 zip object로만 저장되기 때문에 zip묶음을 list나 dict로 한번에 둘러싸서 생성할것
https://coding-kindergarten.tistory.com/tag/python%20zip%20dict
'''