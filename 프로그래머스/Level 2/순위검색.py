'''
인재영입팀에 근무하고 있는 니니즈는 코딩테스트 결과를 분석하여 채용에 참여한 개발팀들에 제공하기 위해
지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.
예를 들어, 개발팀에서 궁금해하는 문의사항은 다음과 같은 형태가 될 수 있습니다.
코딩테스트에 java로 참여했으며, backend 직군을 선택했고, junior 경력이면서,
소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?
즉, 개발팀에서 궁금해하는 내용은 다음과 같은 형태를 갖습니다.
* [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info,
개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return

#############################
방법
정확석 테스트 통과하기 : 매 문의 조건마다 Info배열에서 조건에 해당하는 지원자들을 찾으면서 X점 이상받은 사람 몇명인지 구하기
효율성 테스트 : 위 같은 방식으로 매번 지원자들 찾으면 통과 못함, 지원자들을 그룹별로 적절하게 미리 분류해두면,
              매 문의 조건마다 Info 배열에서 찾지않아도됨
따라서 모든 지원자들을 위와 같은 방식으로 분류한 후 같은 그룹의 지원자끼리 묶어두고,
해당 그룹에서 점수를 기준으로 오름차순 정렬
-> 이제, 검색 조건이 주어질 경우 INFO 배열에서 지원자들을 찾지 않고,
미리 분류해둔 그룹에서 X점 이상 맞은 지원자 수를 세주기만 하면 됨

이때, X점 이상 맞은 지원자를 찾기 위해 해당 그룹의 최저점, 혹은 최고점부터 순차적으로 검색한다면 여전히 오랜 시간이 걸리게 됩니다.
이때, 숫자가 오름차순으로 정렬된 배열에서 X라는 숫자를 찾는 효율적인 방법으로 binary search를 사용할 수 있음음

이때, 배열에 X가 없을 수도 있으므로, 배열에서 X보다 크거나 같은 숫자가 처음 나타나는 위치를 찾아야 하며,
이는 lower bound를 이용하면 됩
'''

from collections import defaultdict
def solution(info, query):
    global answer
    answer = []
    dict = defaultdict(list)
    return dict

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
for i in range(len(info)):
    infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
    mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
    myval = infol[-1]  # info의 점수부분을 value로 분류