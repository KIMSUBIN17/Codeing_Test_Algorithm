def solution(bin1, bin2):
    answer = ''
    a = int(bin1, 2)
    b = int(bin2, 2)
    answer = bin(a+b)
    return answer.replace("0b","")
    #return answer[2:] 도 가능
    # 2진수 앞에 붙는 0b자르기 위해 슬라이싱함
    