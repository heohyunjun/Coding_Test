'''
Ax+By+C로 표현할 수 있는 n개의 직선이 주어질때, 직선의 교점 중 정수 좌표에 별을 그리려고함
직선 A, B, C에 대한 정보가 담긴 배열 line이 매개변수로 주어집니다.
이때 모든 별을 포함하는 최소 사각형을 return
'''
from itertools import combinations as cb
def solution(line):
    line_index = [i for i in range(len(line))]
    list_x_y = []
    list_x, list_y = [], []
    for l1,l2 in cb(line_index, 2):
        a, b, e = line[l1]
        c, d, f = line[l2]
        if (a*d - b*c):
            x = (b*f - e*d)/(a*d - b*c)
            y = (e*c - a*f)/(a*d - b*c)
            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                list_x_y.append((x, y))
                list_x.append(x)
                list_y.append(y)

    x_max, x_min = max(list_x), min(list_x)
    y_max, y_min = max(list_y), min(list_y)
    x_size = x_max - x_min + 1
    y_size = y_max - y_min + 1
    board = [ ['.'] * x_size for _ in range(y_size)]
    for x, y in list_x_y:
        board[y_max-y][x-x_min] = '*'
    return [''.join(s) for s in board]
