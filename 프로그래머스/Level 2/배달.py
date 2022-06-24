'''
마을의 개수 N, 각 마을을 연결하는 도로의 정보 road,
음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
음식 주문을 받을 수 있는 마을의 개수를 return
'''
import heapq
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


def solution2():
    return None