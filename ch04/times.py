# 변수의 유효범위 연습 문제
# 1 ~100 까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의하시오.
# 배수를 구하는 함수를 정의하고 사용
# 배수의 개수 구하기

"""
for i in range(1, 10):
    if i % 2 == 0:
        print(i, end=' ')
"""

def times(x):
    global  count # 전역 변수
    for i in range(1, 101):
        if i % x == 0:
            count += 1
            print(i, end=' ')

count = 0
times(3)
print("\n배수의 개수 : %d" % count)