'''
가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다.
체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.
체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때,
n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return
'''

def is_possible(x, y, n, graph):
    for i in range(x):
        if y == graph[i] or abs(y-graph[i]) == x-i:
            return False
    return True

def queen(x, n ,graph):
    if x ==n: return 1
    cnt = 0

    for y in range(n):
        if is_possible(x, y, n, graph):
            graph[x] = y
            cnt += queen(x+1, n, graph)
    return cnt

def solution(n):
    graph = [0] * n
    answer = queen(0, n, graph)
    return answer
