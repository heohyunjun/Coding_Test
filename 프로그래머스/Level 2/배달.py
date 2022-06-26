'''
마을의 개수 N, 각 마을을 연결하는 도로의 정보 road,
음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
음식 주문을 받을 수 있는 마을의 개수를 return
'''
import heapq
from collections import defaultdict, deque
import sys
def solution(N, road, K):
    answer = 0
    arr = [[]for _ in range(N+1)]
    for a, b, time in road:
        arr[a].append((time, b))
        arr[b].append((time, a))
    visited = [sys.maxsize] * (N+1)
    dijkstra(arr, visited)

    return len([x for x in visited if x <= K])


def dijkstra(arr, visited):
    q = []
    heapq.heappush(q, (0, 1))
    visited[1] = 0
    while q:
        cost, node = heapq.heappop(q)
        if visited[node] > cost:
            continue
        for ncost, nnode in arr[node]:
            temp = cost + ncost
            if visited[nnode] > temp:
                visited[nnode] = temp
                heapq.heappush(q, (temp, nnode))

def solution2(n, road, k) :
    graph = defaultdict(list)
    for v1, v2, dis in road :
        graph[v1].append((v2, dis))
        graph[v2].append((v1, dis))

    visited = [0 for _ in range(n + 1)]
    q = deque([(1, 0)])
    visited[1] = 1

    while q :
        node, dis = q.popleft()

        for v, w in graph[node] :
            if dis + w <= k and (not visited[v] or dis + w <= visited[v]) :
                q.append((v, dis + w))
                visited[v] = dis + w

    answer = n + 1 - visited.count(0)

    return answer