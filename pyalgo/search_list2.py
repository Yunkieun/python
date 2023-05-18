# 순차 탐색
# 학생 번호에 해당하는 이름을 순차 탐색으로 찾아
# 돌려주는 함수를 작성하시오.(단, 학생번호가 없으면 '?'를 반환함)

def search_list(a, x):
    n = len(v)
    for i in range(0, n):
        if a[i] == x:
            return i
        return -1



v = [60, 5, 33, 12, 97]
name = ['이순신', '강감찬', '서희', '안중근', '유관순']

# 매개변수 - 리스트, 찾는값
print(search_list(v, 5))  # 1
print(search_list(v, 12))  # 3
print(search_list(v, 100))  # 3


