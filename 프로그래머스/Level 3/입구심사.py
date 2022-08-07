'''
n명이 임국 심사를위해 줄을 서서 기다리고 있음
처음에 모든 심사대는 비어있음

한 심사대에서는 동시에 한 명만 심사를 할 수 있음
가장 앞에 서있는 사람은 비어 있는 심사대로 가서 심사를 받음
하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로가서 심사 받음

심사 시간을 최소로 하고싶음
입국 심사 기다리는 사람 수 : n
각 심사관이 한 명을 심사하는데 걸리는 시간 : times
모든 사람이 심사를 받는데 걸리는 시간의 최솟값 return
'''

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) *n
    while left<=right:
        mid = (left+right) //2
        checked = 0
        for time in times:
            checked += mid//time
            if checked >=n:
                break

        if checked >=n:
            answer = mid
            right = mid -1
        elif checked <n:
            left = mid+1
    return answer