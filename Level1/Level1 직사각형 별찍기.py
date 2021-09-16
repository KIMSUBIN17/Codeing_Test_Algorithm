/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12969 */

n,m = map(int, input().strip().split(' '))

#range(시작,끝+1)
#1~9라면 range(1,10)이라 작성
for i in range(1, m+1):
    print("*" * n)
    