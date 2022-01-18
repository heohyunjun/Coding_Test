# -*- coding: utf-8 -*-
"""
# 소수 만들기

- 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 

- 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

nums = [1,2,7,6,4]

def solution(nums):
  list_ = list(combinations(nums,3))
  sum_ = [sum(i)  for i in list_]
  not_sosu_ = []
  for i in sum_:
    for j in range(2, int(i//2) +1):
      if i % j == 0:
        not_sosu_.append(i)
        break
  return len(sum_) - len(not_sosu_)

solution(nums)