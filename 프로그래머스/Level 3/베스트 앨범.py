"""
스트리밍 사이트에서 장르별로 가장 많이 재생된 노래를 2개씩 모아 베스트 앨범을 출시
노래는 고유 번호로 구분
노래 수록 기준
1. 속한 노래가 많이 재생된 장르 먼저 수록
2. 장르 내 많이 재생된 노래 먼저 수록
3. 장르 내에서 재생 횟수 같은 노래 중, 고유 번호 낮은거부터 수록
노래의 장르를 나타내는 genres 배열
노래 재생 횟수를 나타내는 plays 배열
베스트 앨범에 들어갈 노래의 고유 번호 순서대로 return
"""
from collections import defaultdict


def solution(genres, plays):
    dict_i_pg = defaultdict(list)
    dict_sum = dict.fromkeys(genres, 0)
    answer = []

    for i, (g, p) in enumerate(zip(genres, plays)):
        dict_i_pg[g].append((i, p))
        dict_sum[g] += p
    for (g, _) in sorted(dict_sum.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(dict_i_pg[g], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer