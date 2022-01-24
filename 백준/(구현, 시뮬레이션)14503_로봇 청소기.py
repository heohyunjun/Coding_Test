# -*- coding: utf-8 -*-
"""
# 로봇 청소기

- 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며 1×1크기의 정사각형 칸으로 나누어져 있다.

- 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다

로봇 청소기는 다음과 같이 작동한다.

- 현재 위치를 청소한다.

- 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.

- 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.

- 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.

- 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.

- 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

- 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
"""

# sol1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N , M = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]


def solution(x, y, d):
    global count
    head = d
    for _ in range(4):
        head = (head + 3) % 4

        new_x = x + dx[head]
        new_y = y + dy[head]

        if map[new_x][new_y] == 1:
            continue
        
        if 0<= new_x<N and 0<= new_y <M and map[new_x][new_y] == 0:
            map[new_x][new_y] = 2
            count +=1
            solution(new_x, new_y, head)
            return
    head = (head +2 ) % 4
    new_x = x + dx[head]
    new_y = y + dy[head]

    if map[new_x][new_y] == 1:
        return
    else:
        solution(new_x, new_y, d)
count = 1
map[r][c] = 2        
solution(r,c,d)
print(count)

# sol2
n,m=map(int, input().split())
r,c,d=map(int, input().split())
dr=[-1, 0, 1, 0]
dc=[0, 1, 0, -1]
wall=[list(map(int, input().split())) for _ in range(n)]
ans=1
wall[r][c]=2
while True:
    turn=0
    while turn < 4:
        d=(d+3)%4
        nr = r + dr[d]
        nc = c + dc[d]
        if wall[nr][nc] == 0:
            r=nr
            c=nc
            wall[r][c]=2
            ans+=1
            break
        turn+=1
    if turn == 4:
        nr=r+dr[(d+2)%4]
        nc=c+dc[(d+2)%4]
        if wall[nr][nc] == 1:
            break
        else:
            r=nr
            c=nc
print(ans)