'''
두 개의 단어 begin, target과 단어 집합 words가 있음
begin -> target으로 변하는 과정
1 한 번에 한 개의 알파벳만 바꿀 수 있음
2. words에 있는 단어로만 변환 가능
예시
begin :"hit",
target : cog",
words : ["hot","dot","dog","lot","log","cog"]
"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환
'''


from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque([])
    q.append([begin, 0])
    while q:
        x, cnt = q.popleft()
        if x==target:
            return cnt
        for i in range(len(words)):
            diff_cnt = 0
            word = words[i]
            for j in range(len(word)):
                if x[j] != word[j]:
                    diff_cnt +=1
            if diff_cnt ==1:
                q.append([word, cnt+1])

    return 0