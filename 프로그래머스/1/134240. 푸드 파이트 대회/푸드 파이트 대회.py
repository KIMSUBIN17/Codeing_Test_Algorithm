def solution(food):
    answer = ''        #가운데는 항상 '0'이 와야함 
    for i in range(1,len(food)):
        #현재 음식의 종류를 나타내는 숫자 i를 문자열로 변환 후,
        #해당 음식의 개수를 반으로 나눈만큼 이어붙임(두 선수가 공평하게 나눠먹을수있도록; food[i]=4라면 2,2씩)
        #그 값을 str(i)랑 곱하면, 현재 음식의 종류를 나타내는 문자열을 해당 음식의 개수만큼 음식의 종류와 개수를 문자열로 이어붙이는 것
        answer += str(i)*(food[i] // 2)
    temp = ''.join(reversed(list(answer)))    
    #temp:상대방 음식
    return answer +'0'+ temp