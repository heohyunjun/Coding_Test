"""
관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중,
다음 두 성질을 만족하는 것을 후보 키(Candidate Key)
유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 함
최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미

즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 함
제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.
릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때,
이 릴레이션에서 후보 키의 개수를 return 하도록 solution
"""
from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final)
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)