/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12947 */

#string형 배열 seoul이 매개변수로 주어짐
def solution(seoul):
    #seoul에서 Kim의 인덱스를 저장할 변수 선언
    n = seoul.index('Kim')
    return '김서방은 {0}에 있다'.format(n)

'''
#풀이
1. seoul안에 Kim이라는 원소가 포함되어 있다는 조건이 있으므로 index('Kim')을 이용해 위치를 인덱싱한 값을 변수 n에 넣음
2. format()을 사용해 바로 리턴

----------------


문제 설명
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.
입출력 예
seoul	return
["Jane", "Kim"]	"김서방은 1에 있다"


#다른 사람 풀이
1. n변수 만들지 않고 바로 format()함수안에 넣음
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

2. f문자열 포매팅

def solution(seoul):
    n = seoul.index('Kim')
    answer = f'김서방은 {n}에 있다'
    return answer


----------
#문자열 포매팅 (참고 문서 : https://wikidocs.net/13)
"현재 온도는 18도입니다." , "현재 온도는 20도입니다" 이라는 두 문장이 있을 때
문자열은 모두 같고 숫자만 달라진다 
-> 문자열 안의 특정한 값을 바꿔야할 경우 "문자열 포매팅 기법"사용
-> 문자열 포매팅 : 문자열 안에 어떤 값을 삽입하는 방법

1. 숫자 바로 대입
>>> "I eat %d apples." % 3
'I eat 3 apples.'


2. 문자열 바로 대입
문자열 안에 꼭 숫자만 넣으라는 법은 없다. 이번에는 숫자 대신 문자열을 넣어 보자.

>>> "I eat %s apples." % "five"
'I eat five apples.'
※ 문자열을 대입할 때는 앞에서 배운 것처럼 큰따옴표나 작은따옴표를 반드시 써주어야 한다.

3. 숫자 값을 나타내는 변수로 대입
>>> number = 3
>>> "I eat %d apples." % number
'I eat 3 apples.'

4. 2개 이상의 값 넣기
문자열 안에 1개가 아닌 여러 개의 값을 넣고 싶을 때
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

#format() 함수 사용한 포매팅
숫자 바로 대입하기

>>> "I eat {0} apples".format(3)
'I eat 3 apples'
"I eat {0} apples" 문자열 중 {0} 부분이 숫자 3으로 바뀌었다.

문자열 바로 대입하기

>>> "I eat {0} apples".format("five")
'I eat five apples'
문자열의 {0} 항목이 five라는 문자열로 바뀌었다.

숫자 값을 가진 변수로 대입하기

>>> number = 3
>>> "I eat {0} apples".format(number)
'I eat 3 apples'
문자열의 {0} 항목이 number 변수 값인 3으로 바뀌었다.

2개 이상의 값 넣기

>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'
2개 이상의 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다. 즉 위 예에서 {0}은 format 함수의 첫 번째 입력값인 number로 바뀌고 {1}은 format 함수의 두 번째 입력값인 day로 바뀐다.

이름으로 넣기

>>> "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'
위 예에서 볼 수 있듯이 {0}, {1}과 같은 인덱스 항목 대신 더 편리한 {name} 형태를 사용하는 방법도 있다. {name} 형태를 사용할 경우 format 함수에는 반드시 name=value 와 같은 형태의 입력값이 있어야만 한다. 위 예는 문자열의 {number}, {day}가 format 함수의 입력값인 number=10, day=3 값으로 각각 바뀌는 것을 보여 주고 있다.

인덱스와 이름을 혼용해서 넣기

>>> "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'
위와 같이 인덱스 항목과 name=value 형태를 혼용하는 것도 가능하다.

f 문자열 포매팅
파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다. 파이썬 3.6 미만 버전에서는 사용할 수 없는 기능이므로 주의해야 한다.

다음과 같이 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.

>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
f 문자열 포매팅은 위와 같이 name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다. 또한 f 문자열 포매팅은 표현식을 지원하기 때문에 다음과 같은 것도 가능하다.

※ 표현식이란 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용하는 것을 말한다.

>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'


'''