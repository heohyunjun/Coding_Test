# -*- coding: utf-8 -*-
"""

# 예산

- 물품 구매시 각 부서가 신청한 금액만큼을 모두 지원해야함
- 예를 들어 1000원을 신청한 부서에는 정확히 1000원을 지원, 1000원보다 적은 금액을 지원해 줄 수는 없음

- 부서별로 신청한 금액이 들어있는 배열d와 예산 budget이 매개변수로 주어질 떄. 최대 몇 개의 부서에 물품을 지원할 수 있는지 return
"""

d = [1, 3, 2, 5, 4]
budget = 10

d.sort()

def solution(d, budget):
  result = 0
  d.sort()
  if budget >= i:
    budget =  budget -i
    result += 1
  return answer