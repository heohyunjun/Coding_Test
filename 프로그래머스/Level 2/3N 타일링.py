'''
가로 길이가 2이고 세로의 길이가 1인 직사각형 모양의 타일이 있습니다.
이 직사각형 타일을 이용하여 세로의 길이가 3이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다.
타일을 채울 때는 다음과 같이 2가지 방법이 있습니다

타일을 가로로 배치 하는 경우
타일을 세로로 배치 하는 경우
직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return
'''

def solution(n):
    answer = [0, 3, 11]
    idx = int(n/2)
    if n%2 !=0:
        return 0
    if idx<3:
        return answer[idx]

    for x in range(3, idx+1):
        answer.append((answer[x-1] * 3 + sum(answer[1: x-1]) * 2 +2)%1000000007)
    return answer[idx]