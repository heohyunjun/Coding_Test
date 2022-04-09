'''
문제
n개의 음이 아닌 정수들있는데 순서바꾸지 않고 더하거나 빼서 target넘버를 만들려고함
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있음.
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

'''
def solution(numbers, target):
    base_ = [0]
    for i in numbers:
        tmp = []
        for j in base_:

            # +, -
            tmp.append(j + i)
            tmp.append(j - 1)
        base_ = tmp
    return base_.count(target)

# bfs로도 풀어보기
# 각 노드에 인덱스를 부여해서 더하기

'''
아이디어
방문한 원소값과 그에 해당하는 index값을 같이 큐에 추가해서 bfs방식으로 해결
'''
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    # 처음 경우의수 ([1, 0] , [-1 , 0] )
    # +1의 인덱스 0, -1 과 인덱스 0
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()

        # 계산을 하면 다음 노드로 넘어가니까, 인덱스 +1
        idx += 1

        # 총 5번 계산만 해야함
        if idx < n:
            # +1 ,-1을 각각해주고 인덱스와 같이 다시 큐에 추가한다
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        # target값이랑 같으면 +1
        else:
            if temp == target:
                answer += 1
    return answer