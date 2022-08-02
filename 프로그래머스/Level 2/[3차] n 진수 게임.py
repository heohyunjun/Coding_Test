'''
여러 사람이 둥글에 앉아서 숫자를 하나씩 차례대로 말하는 게임이 있음
규칙
1. 숫자를 0부터 차례대로 말함.
2. 10 이상의 숫자부터는 한자리씩 끊어서 말함

게임 진행 할 경우
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4...

이진수로 할 경우
0, 1, 1, 0, 1....

자신이 말해야하는 숫자를 출력하는 프로그램 만들기
진법 : n
미리 구할 숫자 개수 t
게임 참가 인원 : m
튜브 순서 : p

10~15는 A~F로
'''

def change_n(num, n):
    ret = ''
    if num == 0:
        return 0
    while num>0:
        num, mod = divmod(num, n)
        ret+=str(info[mod])
    return "".join(list(reversed(ret)))

info = []
for i in range(16):
    if i > 9: info.append(chr(i+55))
    else: info.append(str(i))

def solution(n, t, m, p):
    answer = '0'
    for i in range(1, t*m):
        answer+=change_n(i, n)

    return answer[p-1 : t*m : m]