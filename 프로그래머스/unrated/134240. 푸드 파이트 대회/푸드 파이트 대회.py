def solution(food):
    answer = ''        #가운데는 항상 '0'이 와야함 
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    temp = ''.join(reversed(list(answer)))    
    #temp:상대방 음식
    return answer +'0'+ temp