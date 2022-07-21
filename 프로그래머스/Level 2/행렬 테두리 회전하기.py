'''
row * colums 크기의 행렬이 있음
이 행렬에서 직사각형 모양의 범위를 여러 번 선택해,
테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 함
각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 아래와 같음
x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전
행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때,
각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return
'''
def solution(rows, columns, queries):
    answer = []
    board = []
    for i in range(rows):
        board.append([map_ for map_ in range(i*columns+1, (i+1)*columns+1)])

    for x1, y1, x2, y2  in queries:
        left_top = board[x1-1][y1-1]
        min_value = left_top

        for left_ in range(x1-1, x2-1):
            tmp = board[left_+1][y1-1]
            board[left_][y1-1] = tmp
            min_value = min(min_value, tmp)

        for bottom_ in range(y1-1, y2-1):
            tmp = board[x2-1][bottom_+1]
            board[x2-1][bottom_] = tmp
            min_value = min(min_value, tmp)

        for right_ in range(x2-1, x1-1, -1):
            tmp = board[right_-1][y2-1]
            board[right_][y2-1] = tmp
            min_value = min(min_value, tmp)

        for top_ in range(y2-1, y1-1, -1):
            tmp = board[x1-1][top_-1]
            board[x1-1][top_] = tmp
            min_value = min(min_value, tmp)
        board[x1-1][y1] = left_top
        answer.append(min_value)
    return answer