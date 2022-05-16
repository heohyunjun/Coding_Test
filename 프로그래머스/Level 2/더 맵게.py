'''
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶어함
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을
아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듬
섞은 음식의 스코빌 지수 =
    가장 맵지 않은 음식의 스코빌 지수 +
    (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞음
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
'''
scoville = [1, 2, 3, 9, 10, 12]

import heapq
def calc(x :list):
    pop_1 = heapq.heappop(x)
    pop_2 = heapq.heappop(x)
    value = pop_1 + pop_2 * 2
    heapq.heappush(x, value)
    return x

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >1:
        scoville = calc(scoville)
        answer+=1
    return answer if scoville[0]>K else -1