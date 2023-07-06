# 유튜브 강의 참고
# https://velog.io/@greene/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL0-%EB%8B%A4%ED%95%AD%EC%8B%9D-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(polynomial):
    xnum = 0    #항
    const = 0   #정수
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
    
'''
공백기준 split대신 ' + ' 공백과 +을 함께 묶어서 split
'''
 