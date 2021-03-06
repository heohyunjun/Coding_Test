# -*- coding: utf-8 -*-
"""

## 개미전사
- 식량 창고는 일직선
- 개미 전사는 선택적으로 식량창고를 빼앗을 예정
- 이떄 메두끼 정찰병들은 일직선상에 존재하는 식량 창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알 수 있음
- 따라서 개미 전사가 들키지 않고 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야함
- 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성
"""

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
print(d[n-1])

