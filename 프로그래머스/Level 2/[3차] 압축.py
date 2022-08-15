'''
메시지 압축해야함
알고리즘 중 성능이 좋은 간단한 LZM 사용

LZM 압축과정
1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
3. w에 해당하는 사전의 색인 번호 출력하고 입력에서 w제거
4. 입력에서 처리되지 않은 다음 글자가 남아 있다면(c), w+c에 해당하는 단어를 사전에 등록
5. 2단계로 돌아감


'''
def solution(msg):
    alp = {chr(i+64) : i for i in range(1, 27)}
    idx = len(alp) + 1
    start, end = 0, 1
    answer = []
    while end < len(msg) + 1:
        s = msg[start:end]
        if s in alp:
            end+=1
        else:
            answer.append(alp[s[:-1]])
            start = end-1
            alp[s] = idx
            idx+=1
    answer.append(alp[s])
    return answer