#과목의 개수 N입력
N=int(input())

#각 과목의 현재 성적 입력받기
scores = list(map(int, input().split())) 

#점수 중 가장 큰 값 구하기
M = max(scores)

#각 점수를 점수/M*100으로 변환
new_scores = [(score / M) * 100 for score in scores]
new_avg = sum(new_scores) / N
print(new_avg)