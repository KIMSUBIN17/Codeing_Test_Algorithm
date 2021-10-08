/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/1845 */

def solution(participant, completion):
    
    #participant리스트와 completion리스트를 같은 방향으로 정렬
    participant.sort()
    completion.sort()
    #completion 리스트 길이만큼 탐색
    for i in range(len(completion)):
        #completion리스트 길이만큼 탐색할 때 completion리스트와 같지 않은 경우 = 완주하지 못한 선수
        if participant[i] != completion[i]:
            return participant[i]
        
        #탐색이 끝나면 participant의 마지막 요소가 완주하지 못한 선수이기 때문에 pop으로 꺼냄    
    return participant.pop()

'''
#풀이
1. 참가자 배열과 완주자 배열의 원소(선수)를 비교해야 하기 때문에 sort를 사용해서 같은 방향으로 정렬해줌(비교하기 쉬우려고)
2. sort한 상태에서 완주자 리스트길이만큼 탐색을 진행

3. 참가자배열 인덱스값과 완주자 배열인덱스값이 다른 것이 나오면
-> 그 참가자는 완주자 명단에 없다는 뜻 => 완주하지 못한 사람으로 출력

4. 완주자 배열을 다 확인했는데 참여자 배열과 같다면
-> 참여자 배열 가장 마지막에 있는 사람 => 완주하지 못한 사람으로 출력
 완주하지 못한 선수(=참가자)->중복 참가자의 경우
맨 마지막 값으로 pop으로 꺼내서 return 



#다른 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

*counter 사용
딕셔너리 형태로 변환해 counter로 각 문자를 카운팅함
그리고 participant에서 completion을 빼면 완주하지 못한 사람을 출력가능



--------------------
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
입출력 예
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

입출력 예 #2
6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리, 2번 폰켓몬 한 마리, 4번 폰켓몬 한 마리를 고르면 되며, 따라서 3을 return 합니다.


입출력 예 #3
6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리와 2번 폰켓몬 두 마리를 고르거나, 혹은 3번 폰켓몬 두 마리와 2번 폰켓몬 한 마리를 고르면 됩니다. 따라서 최대 고를 수 있는 폰켓몬 종류의 수는 2입니다.

'''
