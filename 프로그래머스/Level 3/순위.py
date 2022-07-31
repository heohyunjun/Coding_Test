'''
n명의 권투 선수가 권투 대회에 참여했고 각각 1번부터 n번 까지 번호를 받음
권투는 1대1방식으로 진행,
A가 B보다 실력이 좋으면, A가 항상 이김
심판은 주어진 경기결과를 가지고 선수들의 순위를 매기려함
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길수 없음
선수의 수 n
경기 결과를 담은 2차원 배열 results가 매개 변수로 주어질 떄,
정확하게 순위를 매길 수 있는 선수의 수를 return
'''
from collections import defaultdict
def solution(n, results):
    answer=0
    winner = defaultdict(set)
    loser  = defaultdict(set)

    for win, lose in results:
        winner[lose].add(win)
        loser[win].add(lose)

    for i in range(1, n+1):
        for win in winner[i]:
            loser[win].update(loser[i])
        for lose in loser[i]:
            winner[lose].update(winner[i])
    for i in range(1, n+1):
        if len(winner[i]) +len(loser[i]) == n-1:
            answer+=1

    return answer
