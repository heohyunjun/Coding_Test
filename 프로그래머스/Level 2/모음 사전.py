'''
title : 모음 사전

사전에 알파벳 모음 'A', 'E', 'I', 'O', 'I', 'U'만 사용해서 만들 수있는 모든 단어가 있음
사전의 첫번째 단어는 'A', 그다음은 'AA', 마지막 단어는 'UUUUU'

word 길이는 1이상 5이하

단어 하나 word가 매개변수로 주어질 때, 사전에서 몇 번쨰 단어인지 리턴

아이디어 : 단순하게 사전 다 만들어서 인덱스 찾음
'''

# from itertools import product
def solution(word):

    dict_ = []
    for i in range(1,6) :
        dict_ += list(map(''.join, product("AEIOU", repeat = i)))
    dict_.sort()

    answer = dict_.index(word) + 1

    return answer