'''
야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한값
Demi는 N시간 동안 야근 피로도를 최소화하도록 일할예정
1시간동안 작업량 1만큼을 처리가능하다고 할 때, 퇴근까지 남은 N시간과 일에 대한 작업량 works에 대해 야근
피로도를 최소화한 값을 리턴
'''

import heapq
def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return 0
    answer = 0

    works = [-w for w in works]
    heapq.heapify(works)
    while n >0:
        max_ = heapq.heappop(works)
        heapq.heappush(works, max_+1)
        n-=1
    for i in works:
        answer+=i**2
    return answer