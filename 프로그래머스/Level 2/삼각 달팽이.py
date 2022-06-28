'''
정수 n이 매개변수로 주어집니다.
다음 그림과(그림생략) 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return
'''


def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 오른쪽
                y += 1
            elif i % 3 == 2:  # 위
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j:
                answer.append(j)
    return answer
