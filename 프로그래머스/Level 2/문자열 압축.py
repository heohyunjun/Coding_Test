'''
문자열 압축
문제
----
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더
짧은 문자열로 줄요서 표현하고자함
ex) aabbaccc -> 2a2ba3c 의  방식으로 처음했지만 압축률이 적음
그래서 ababcdcdababcdcd의 경우 3개 단위로 자르면, 2abcdede가 도어 가장 짧은압축이됨
압축한 문자열 s가 매개변수로 주어질때, 위와 같은 방법으로 1개 이상단위로 문자열을 잘라
압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return

'''
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        compressed = ''
        prev = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if prev==s[j:j+i]:
                count+=1
            else:
                compressed+=str(count) + prev if count >= 2 else prev
                prev = s[j:j+i]
                count = 1
        compressed+=str(count)+prev if count>=2 else prev
        answer = min(answer, len(compressed))

    return answer