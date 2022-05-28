'''
1과 0으로 채워진 표(board)가 있음
ex)
 0 1 1 1
 1 1 1 1
 1 1 1 1
 0 0 1 0
이떄 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return

# 동적프로그래밍으로 풀어야할것같긴함
#
'''
def solution(board):
    n = len(board)
    m = len(board[0])

    # dp 준비
    dp = [[0] * m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1, n):
        dp[i][0] = board[i][0]

    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer ** 2


def solution(board):
    n = len(board)
    m = len(board[0])

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) +1

    answer = 0
    for max_ in board:
        answer = max(max(max_), answer)
    return answer ** 2

