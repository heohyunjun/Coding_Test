# -*- coding: utf-8 -*-
"""
# 소수 찾기

문제 설명

- 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 

- 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

- 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
"""

from itertools import permutations as pm

def is_Prime(n):
    if n < 2: 
        return False

    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        num_list = list(map(''.join, pm(list(numbers), k)))
   
        for i in list(set(num_list)):
            if is_Prime(int(i)):
                answer.append(int(i))
                
    answer = len(set(answer))

    return answer

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    print(a)
    a -= set(range(0, 2))
    print(a)
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

numbers = "011"
solution(numbers)