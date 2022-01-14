# -*- coding: utf-8 -*-
"""
# 모의고사
"""

answers= [1,3,2,4,2]

# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
        math1 = [1 , 2, 3, 4, 5]
        math2 = [2, 1, 2, 3, 2, 4, 2, 5]
        math3= [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        score = [0 ,0 ,0]
        result =[]
        for i in range(len(answers)):
            if math1[i%len(math1)] == answers[i]:
                score[0] += 1

            if math2[i%len(math2)] == answers[i]:
                score[1] += 1

            if math3[i%len(math3)] == answers[i]:
                score[2] +=1
        for i in range(len(score)):
            if score[i] == max(score):
                result.append(i+1)
        return result

solution(answers)