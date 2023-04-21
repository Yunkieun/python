# 수학 모듈 - math
# 절대값, 올림, 내림, 제곱근, 원주율
import math

print(math.pi) # 원주율
print(math.ceil(2.54)) # 정수로 올림
print(math.floor(4.923)) # 내일(버림)
print(math.sqrt(25)) # 제곱근


# 내장 함수
print(round(11.78))
# 절대값
print(abs(-10))

# 절대값을 함수로 만들기
"""
def my_abs(x):
    if x < 0:
        return -x
    else:
        return  x

print(my_abs(-5)) # -5 -> -(-5), 5 -> 5
"""

# 2. 알고리즘2
def my_abs2(x):
    y = x * x
    return math.sqrt(y)

# 제곱수 -> 제곱근
print(int(my_abs2(-5)))
print(int(my_abs2(5)))










