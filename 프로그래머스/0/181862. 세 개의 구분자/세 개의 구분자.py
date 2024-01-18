def solution(myStr):
    answer = []
    #문자열 myStr에 a,b,c를 순서대로 찾아서 있다면 그 자리를 공백으로 변경하고, myStr에 새로 담음
    for i in ['a','b','c']:
        myStr = myStr.replace(i, ' ')
    #공백으로 변경된 것들을 공백을 기준으로 split해서 answer에 리스트 형태로 담고 
    answer = myStr.split()
    #answer에 없으면 ['EMPTY']를 리턴함(문제요건)
    if not answer:
        answer = ['EMPTY']
    return answer