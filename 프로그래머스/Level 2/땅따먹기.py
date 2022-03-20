'''
다이나믹 프로그래밍 사용
원하는 경우의 수를 저장해두고 다시 계산을 하지 않는다.
'''
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[-1])


solution(land)