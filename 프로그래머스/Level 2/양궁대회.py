'''
양궁대회 규칙
1. 어피치가 화살 n발 다 손후에 라이언이 화살 n발을 쏨
2. 점수를 계산
점수 계산법
- 더 많은 화살을 k점에 맞힌 선수가 k점을 가져감
- 둘이 똑같이 쏘면 어피치가 점수 득, 둘다 못맞추면 0
3. 점수 높으면 승리, 점수 같으면 어피치 승리

현재 상황
1. 어피치가 화살 n발을 다쏘고 라이언이 쏠 차례
2. 라이언은 큰 점수차로 이기기 위해 n발의 화살을 쏠것

화살 개수 담은 자연수 : n
어피치가 맞힌 과녁 점수 : info
라이언이 우승할수 없는 경우 : -1
'''
from collections import deque
def bfs(n, info):
    max_gap = 0
    result =[]
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])

    while q:
        arrow_cnt, target = q.popleft()
        if sum(target) == n:
            apeach, lion=0,0
            for i in range(11):
                if not (info[i] ==0 and target[i] == 0):
                    if info[i]>=target[i]:
                        apeach+=10-i
                    else:
                        lion +=10-i
            if apeach <lion:
                gap = lion-apeach
                if max_gap>gap:
                    continue
                if max_gap<gap:
                    max_gap=gap
                    result.clear()
                result.append(target)
        elif sum(target) >n:
            continue
        elif arrow_cnt==10:
            tmp = target.copy()
            tmp[arrow_cnt]=n-sum(tmp)
            q.append((-1, tmp))
        else:
            tmp = target.copy()
            tmp[arrow_cnt] =info[arrow_cnt]+1
            q.append((arrow_cnt+1, tmp))

            tmp2 = target.copy()
            tmp2[arrow_cnt]=0
            q.append((arrow_cnt+1, tmp2))
    return result



def solution(n, info):
    answer = bfs(n, info)
    if not answer:
        return [-1]
    elif len(answer) ==1:
        return answer[0]
    else:
        return answer[-1]