# -*- coding: utf-8 -*-
"""

# 주식 가격

- 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 

- 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

하나 뽑고
뒤에꺼 비교
"""

prices = [1, 2, 3, 2, 3]

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        a = prices.popleft()
        cnt = 0
        for i in prices:
            if a > i:
                cnt += 1
                break
            cnt +=1
        answer.append(cnt)
    return answer

solution(prices)

answer