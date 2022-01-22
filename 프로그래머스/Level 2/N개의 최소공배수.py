# -*- coding: utf-8 -*-
""" N개의 최소 공배수

- 예를 들어 2와 7의 최소공배수는 14가 됩니다. 

- 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 

- n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
"""

arr = [2, 6, 8, 14]
# arr = [1, 2, 3]

def solution(arr):

    max_num = 1
    answer = 0
    for i in arr:
        max_num *= i
    for j in range(2, max_num +1):
        for a in arr:
            if j % a !=0:

                break
        else:
            answer = j
            break
    return answer

solution(arr)

from math import gcd

def solution(arr):
    from math import gcd                           
    answer = arr[0]                                
    for num in arr:                                 
        answer = answer*num // gcd(answer, num)     
    return answer