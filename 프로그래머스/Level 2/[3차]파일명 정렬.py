'''
저장소 서버에는 프로그램의 과거 버전을 모두 담고 있어,
이름 순으로 정렬된 파일 목록은 보기가 불편했다.
파일을 이름 순으로 정렬하면 나중에 만들어진
ver-10.zip이
ver-9.zip보다 먼저 표시되기 때문
["img12.png", "img10.png", "img2.png", "img1.png"]일 경우,
일반적인 정렬은 ["img1.png", "img10.png", "img12.png", "img2.png"] 순이 되지만,
숫자 순으로 정렬된 ["img1.png", "img2.png", "img10.png", img12.png"] 순이 훨씬 자연스러움
HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상
NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며,
앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능
TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있음
파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 이때, 문자열 비교 시 대소문자 구분을 하지 않는다.
MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다.
파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다.
9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다.
숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우,
원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면,
정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.
'''
def solution(files):
    answer = []
    idx = 0
    for file_ in files:
        head, number = "", ""
        check = False

        for s in file_:
            if s.isdigit() and len(number) < 5:
                number +=str(s)
                check =True
            elif not check:
                head+=s.lower()
            else:
                break
        answer.append([head, int(number), idx, file_])
        idx+=1
    answer.sort()
    return [answer[i][3] for i in range(len(answer))]