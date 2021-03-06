'''
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장함
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 떄
서로 다른 옷의 조합의 수를 return

제한사항
clothes의 각행은 [의상 이름, 의상종류]로 이루어짐
같은 이름 의상 없음
clothes 모든 원소는 문자열
'''
from collections import defaultdict
def solution(clothes):
    answer = 1
    dict_ = defaultdict()
    for clothe, type_ in clothes:
        dict_[type_] = dict_.get(type_, 0) + 1

    for type_ in dict_:
        answer *= (dict_[type_] + 1)

    return answer - 1

