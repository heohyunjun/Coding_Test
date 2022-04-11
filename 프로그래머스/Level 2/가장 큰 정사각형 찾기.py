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
    answer = 0
    n = len(board)
    m = len(board[0])
    # dp 준비
    dp = [[0] * m for _ in range(n)]
    dp[0] = board[0]

    return answer

