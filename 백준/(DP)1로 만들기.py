# -*- coding: utf-8 -*-
"""
## 1로 만들기
"""

x = int(input())

# DP 테이블 초기화
d = [0] * 30001

for i in range(2, x + 1):
    # 현재 수에서 1뺴는 경우
    d[i] = d[i-1] + 1

    # 2로 나누어떨어지는경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])

