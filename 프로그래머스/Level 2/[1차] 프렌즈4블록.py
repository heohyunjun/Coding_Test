'''
같은 모양의 카카오프렌즈 블록이 2*2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임
블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 됨
위 과정을 반복
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어옴
2<=n, m<=30
baord는 길이 n인 문자열 m개의 배열로 주어짐

'''
def solution(m, n, board):
    answer = 0

    # board 맵 만들기
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        bomb = []
        for row in range(m-1):
            for col in range(n-1):
                # 터진건 0으로 , 터졋으면 패스
                if board[row][col] == '0':
                    continue
                # 4칸 비교, 같으면 각각 row, col -> bomb리스트에 저장
                if board[row][col] == board[row][col+1]:
                    if board[row][col] == board[row+1][col]\
                    and board[row][col+1] == board[row+1][col+1]:
                        bomb.append((row, col))
                        bomb.append((row, col+1))
                        bomb.append((row+1, col))
                        bomb.append((row+1, col+1))
        # 더이상 터질게 없으면 break
        if len(bomb) == 0:
            break
        # 터질게 있으면
        else:
            # 터진 블록수 추가
            answer +=len(set(bomb))

            # 터트리기 == 0으로 바꾸기
            for b1, b2 in bomb:
                board[b1][b2] ='0'

            # reversed -> 밑에 row부터 처리하기
            for rb1, rb2 in reversed(bomb):
                past = rb1-1
                now = rb1

                while past>=0:
                    if board[now][rb2] == '0' and board[past][rb2] !='0':
                        board[now][rb2] = board[past][rb2]
                        board[past][rb2] ='0'
                        now -=1
                    past -=1
    return answer