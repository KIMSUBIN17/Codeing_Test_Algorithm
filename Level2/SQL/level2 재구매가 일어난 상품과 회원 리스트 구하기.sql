/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131536 */


SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC;


'''
재구매한 회원ID와 재구매한 상품ID를 구하기 위해 GROUP BY로 묶음 

'''

