/*링크 : https://programmers.co.kr/learn/courses/30/lessons/76501 */

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


'''
문제 설명
어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

제한사항
absolutes의 길이는 1 이상 1,000 이하입니다.
absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
signs의 길이는 absolutes의 길이와 같습니다.
signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
입출력 예
absolutes	signs	result
[4,7,12]	[true,false,true]	9
[1,2,3]	[false,false,true]	0
입출력 예 설명
입출력 예 #1

signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
따라서 세 수의 합인 9를 return 해야 합니다.

#풀이
absoultes와 signs의 길이는 같기 때문에 단일 for문으로 동일한 인덱스에서 
signs이 true이면 양수처리, false이면 음수처리하여 답 구함

signs가 참이면 해당 absolutes의 수가 양수, 거짓이면 음수가 됨
주어진 수 하나씩 접근해 양수,음수가 적용된 실제 합 구함
if signs[i] : 참인 경우 양수이므로 answer에 더하고, 거짓인경우에는 음수이므로 빼기


#다른 사람 풀이
1. zip()함수 사용 
- 여러그룹의 데이터를 동시에 반복문으로 처리 가능
- 가장 짧은 데이터 길이만큼 반복

def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer


def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))










'''