# -*- coding: utf-8 -*-
"""
# 가장 큰 수

- 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

- 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
"""

numbers = [6, 10, 2]

def solution(numbers):
    return str(int("".join(sorted(list(map(str, numbers)) , key=lambda x: x * 3, reverse = True))))