# -*- coding: utf-8 -*-
"""
# 올바른 괄호

- '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 

- 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
"""

s = "()()"
print(s[-1])
# s = "((()))("

def solution(s):
    stack = []
    for c in s:
        if c =="(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) ==0

solution(s)