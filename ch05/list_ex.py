# 리스트 복사
a = [1, 2, 3, 4]
a2 = []

"""
for i in a:
    a2.append(3 * 1)
print(a2)
"""

# 리스트 내부에 포함 - for 문이 리스트 내포
a3 = [3 * i for i in a]
print(a3)

a4 = [] # 3의 배수이면서 짝수인 수 저장
"""
for i in a:
    if i % 2 == 0:
        a4.append(3 * i)
"""
a4 = [3 * i for i in a if i % 2 == 0]
print(a4)