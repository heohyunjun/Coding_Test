'''
가로 길이가 Wcm
세로 길이가 Hcm 인 직사각형 종이가 있음
종이는 1*1 정사각형으로 채워져있음

근데 이 종이를 대각선 꼭지점 2개를 잇는 방향으로 잘랐을 경우
안잘린 정사각형 개수
'''

import math
def solution(w, h):
    return w*h - (w+h -math.gcd(w,h))