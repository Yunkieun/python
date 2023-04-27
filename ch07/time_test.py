import time

start = time.time()
def getgob(n):
    gob = 1  # 곱셈에서는 1로 초기화
    for i in range(1, n+1):
        gob *= i
        #print(i, gob)
    return gob

print(getgob(10000))
end = time.time()
print(f"소요 시간 : {end-start}")

# 재귀함수 측정
start = time.time()
def facto(n):
    if n <= 1: # focto(1) = 1
        return 1
    else:
        return n * facto(n-1)
print(facto(995))
end = time.time()
print(f"소요 시간 : {end-start:.20f}")