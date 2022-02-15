# -*- coding: utf-8 -*-
"""
## 다이나믹 프로그래밍 - 피보나치 수열

메모이제이션
- 한 번 계산된 결과를 메모리 공간에 메모
- 캐싱
- 결과저장용 리스트를 DP테이블 이라고 함
- 국한된 개념은 아님
"""

# 탑다운
d = [0] *100
def fibo(x):

    # 종료 조건
    if x ==1 or x == 2:
        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계싼하지 않은 문제라면 재귀적으로 계산
    d[x] = fibo(x-1) + fibo(x-2)
    return  d[x]
print(fibo(99))


# 보텀업
d = [0] *100
d[1] = 1
d[2] = 1
n =99
for i in range(3, n+1):
    d[i] = d[i-1] +d[i-2]
print(d[n])

