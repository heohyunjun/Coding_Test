# -*- coding: utf-8 -*-
"""
# 숫자의 표현

- 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 

- 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
1. 1 + 2 + 3 + 4 + 5 = 15
2. 4 + 5 + 6 = 15
3. 7 + 8 = 15
4. 15 = 15
"""

n = 15

def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer +=1
                break
            if sum > n:
                break
    return answer