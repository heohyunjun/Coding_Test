# -*- coding: utf-8 -*-
"""
# 기능 개발

- 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
- 각 배포마다 몇 개의 기능이 배포되는지를 return
"""

progresses = [93, 30, 55]
speeds = [1, 30, 5]

from collections import deque
def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)

    cnt = 0
    day = 0
    while len(p) >0:
        if p[0] +s[0]*day >=100:
            p.popleft()
            s.popleft()
            cnt +=1
        else:
            if cnt >0:
                answer.append(cnt)
                cnt = 0
            day += 1 
    answer.append(cnt)
    return answer

