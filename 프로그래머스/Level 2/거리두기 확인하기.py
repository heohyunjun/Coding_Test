'''
대기실은 5개, 각 대기실은 5*5
응시자 끼리는 맨해튼 거리가 2이하로 앉으면 안됨
단 응시자가 앉아있는 자리 사이가 파티션으로 막혀있는 경우 허용
응사지달 정보, 대기실 구조르 ㄹ대기실별로 담으 2차원문자배열 places
거리 두기를 지키고 있는 경우 1, 한명이라도 지키지 않은 경우 0 return
'''


from collections import deque
def bfs(place):
    start = []
    dx = [1, -1 , 0, 0]
    dy = [0 , 0, 1, -1]


    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                start.append([row, col])

    for s in start:
        q = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance= [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]]=1

        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx]==0:
                    if place[ny][nx]=='O':
                        q.append([ny, nx])
                        distance[ny][nx] = distance[y][x] +1
                        visited[ny][nx]=1
                    if place[ny][nx] =='P' and distance[y][x]<=1:
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer