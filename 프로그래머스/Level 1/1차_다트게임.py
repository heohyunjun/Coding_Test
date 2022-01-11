# -*- coding: utf-8 -*-

s = '1S2D*3T'

# 전형적인 완전탐색
def solution(x):
  score = []
  
  # 문자열로 하는 이유는 10이 나왔을때 1, 0을 string형태로 더하기 위해서
  num = ''

  for i in x:

    # 문자열인지 실수인지 확인
    if i.isnumeric():
      num += i
    
    # 1승하고 점수 리스트에 추가
    elif i == 'S':
      num = int(num)**1
      score.append(num)

      # 문자열 초기화
      num = ''

    # 2승하고 점수 리스트에 추가
    elif i =='D':
      num = int(num) **2
      score.append(num)

      # 문자열 초기화
      num = ''
    elif i == 'T':
      num = int(num)**3
      score.append(num)
      num = ''
    elif i == '*':
      # score > 1 : *이 맨처음 나왓는지 확인
      if len(score) > 1:  
        score[-2] = score[-2] * 2
        score[-1] = score[-1] * 2
      else:
        score[-1] = score[-1] *2
    elif i == '#':
        score[-1] = score[-1] * -1
    
  return sum(score)

solution(s)

# sol2
def solution(dartResult):
    point = []
    answer = []

    # 10을 k로 치환
    dartResult = dartResult.replace('10','k')

    # k를 다시 '10' 으로 변경
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

s= '1D2S#10S'
solution(s)