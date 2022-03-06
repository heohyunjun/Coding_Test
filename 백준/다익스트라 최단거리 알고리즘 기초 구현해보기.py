# -*- coding: utf-8 -*-
"""

# 다익스트라 알고리즘
"""

# 노드 개수, 간선 개수 입력 받기
n, m = map(int, input().split())


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
    pass