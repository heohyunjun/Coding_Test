# -*- coding: utf-8 -*-
"""
# H-Index

- 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

- 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 

- 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
"""

def solution(citations):
    citations = sorted(citations)
    len_ = len(citations)
    for i in range(len_):
        if citations[i] >= len_-i:
            return len_ - i
    return 0

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer