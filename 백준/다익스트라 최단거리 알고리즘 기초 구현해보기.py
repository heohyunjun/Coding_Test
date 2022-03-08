# 노드 개수, 간선 개수 입력 받기
n, m = map(int, input().split())

# 10억 = 무한 = 1e9
INF = int(1e9)
# 시작 노드
start = int(input())

# 각 노드에 연결된 노드 정보 담는 리스트
graph = [[] for i in range(n + 1)]

# 방문 여부 체크하는 리스트
visited = [False] * (n + 1)

# 최단 거리 테이블 모드 무한으로 초기화
distance = [INF] * (n + 1)

# 방문 하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환하는 함수
def get_smallest_node():
    min_value = INF

    # 가장 최단 거러기 짧은 노드
    index = 0
    for i in range(1, n+ 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[i]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:

                distance[j[0]] = cost
# 다익스트라 실행
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

