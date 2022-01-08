# -*- coding: utf-8 -*-
"""그리디.ipynb


- 두 사람은 두 슬라임을 골라서 하나로 합쳐야함
- 게임은 슬라임이 하나 남았을 떄 끝남
- 두 슬라임 x .y 합치면 크기는 x + y
- 합칠 때 마다 x * y를 얻음
- 점수의 최댓값을 구해라

입력
- 첫재 줄 : 슬라임 개수 N
- 둘째 줄 : 슬라임 크기

출력
- 영선이와 효빈이가 얻을수 있느 점수

아이디어
- 오름차순 정렬해서 더한다
"""

# sol1
# 슬라임 갯수
N = int(input())

# 슬라임 크기
s = list(map(int, input().split()))

# 점수 저장
result = 0

# 슬라임 크기 오름차순 정렬
s.sort()

start = s[0]
for i in range(1,len(s)):
  result += start * s[i]
  start = start + s[i]

print(result)

# sol2
n = int(input())
L = list(map(int,input().split()))
result = 0
while len(L) != 1:
    x, y = L.pop(), L.pop()
    print(x, y)
    result += (x*y)
    L.append(x+y)
print(result)