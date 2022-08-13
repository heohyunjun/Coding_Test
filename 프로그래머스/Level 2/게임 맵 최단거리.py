'''
ROR 게임은 두 팀으로 나누어서 진행하며,
상대 팀 진영을 먼저 파괴하면 이기는 게임입니다.
따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리
게임 맵의 상태 maps가 매개변수로 주어질 때,
캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의
최솟값을 return

maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리
처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치
'''

# bfs
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[x][y] == 1:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx, ny))
    return visited[-1][-1] if visited[-1][-1]>0 else -1
