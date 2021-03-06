'''
단품 메뉴들을 조합해서 코스요리 메뉴를 구성하려고함
이전에 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리로 구성
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하며
최소 2명 이상의 손님으로 부터 주문된 단품 메뉴 조합이어야함

제한 사항
orders 배열 크기는 2이상 20이하, 배열 각 원소는 2 이상 10이하
정답은 오름차순으로 정렬

'''
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for o in orders:
            cb = combinations(sorted(o), c)
            tmp+=cb
        dict_ = Counter(tmp)
        if dict_:
            max_ = max(dict_.values())
            if max_ > 1:
                for k, v in dict_.items():
                    if v == max_:
                        answer.append("".join(k))
    return sorted(answer)