def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0] * 3
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            cnt[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            cnt[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            cnt[2] += 1
    for idx, score in enumerate(cnt):
        if score == max(cnt):
            result.append(idx+1)
    return result
    


'''
풀이방법
주어진 패턴대로 답지를 만들고
답지별로 맞은 개수를 세서 cnt 배열에 저장할 것이므로 cnt배열을 만들고 0으로 초기화함
answer를 돌면서 답지랑 비교해서 정답이면 cnt에 +1
가장 많이 맞춘 사람 = cnt가 큰 사람 = 배열의 첫번째값
(배열인덱스는 0부터 시작이므로 1을 더해서 리턴)
'''