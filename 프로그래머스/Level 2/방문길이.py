'''
U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기
캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
좌표평면의 경계는 왼쪽 위(-5, 5),
왼쪽 아래(-5, -5), 오른쪽 위(5, 5),
오른쪽 아래(5, -5)로 이루어져 있습니다.
명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return
'''

def solution(dirs):
    move_set = set()
    direction = {'U': [0, 1], 'D' : [0, -1], 'R' : [1, 0], 'L' : [-1, 0]}
    answer = 0
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x+direction[dir][0], y+direction[dir][1]
        if -5<=nx<=5 and -5<=ny<=5:
            dis_1 = (nx, ny, x, y)
            dis_2 = (x, y, nx, ny)
            if dis_2 not in move_set:
                move_set.add(dis_1)
                move_set.add(dis_2)
                answer+=1
            x, y =nx, ny
    return answer