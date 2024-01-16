def solution(arr, queries):
    answer = []
    
    for query in queries:
        s,e,k = query
        #각 쿼리에서 시작인덱스(s)~ 종료인덱스(e)에 대한 부분 배열 만들고, sort해서 k보다 가장 작은 수를 골라냄
        sub_arr = arr[s:e+1]
        sub_arr.sort()
        
        
        count = 0
        #sub배열에서 뽑은 num이 k보다 크면, count를 +1
        for num in sub_arr:
            if num > k:
                answer.append(num)
                count += 1
                break
        if count == 0:
            answer.append(-1)        
        
    return answer