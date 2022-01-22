# -*- coding: utf-8 -*-
"""
# JadenCase

- JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 

- 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
"""

s = "3people unFollowed me"	
s= "for the last     week"

def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()

def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)

