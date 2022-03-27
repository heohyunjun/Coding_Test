'''

다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의

(), [], {} 는 모두 올바른 괄호 문자열
1. 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열
    예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.

2. 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.
    예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어짐

이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수 완성
'''


from collections import deque
def solution(s):
    answer= 0
    s = deque(s)
    # 이중 for문 돌기, 한 문자열당 모두 체크
    for _ in range(len(s)):
        stack = []
       # 스택에 넣어서 확인
        # 스택 길이 0이면 추가
        for j in range(len(s)):
            if len(stack) >0 :
                if stack[-1] == "(" and s[j]==")":
                    stack.pop()
                elif stack[-1] =="[" and s[j]=="]":
                    stack.pop()
                elif stack[-1] == "{" and s[j]=="}":
                    stack.pop()
#                 # 스택에 들어있는 것중 마지막 문자열과 계속 비교해서 다르면 문자열 추가
                else:
                    stack.append(s[j])
#             길이가 0이면 추가 == 위 조건문을 일치해서 pop해서 0일 수도 있음
            else:
                stack.append(s[j])
#       # stack 길이가 0 == 괄호들이 다 일치해서 0
        if len(stack) == 0:
            answer+=1
#       # 1이 아닌 경우 == 괄호들이 불일치, 맨앞에꺼를 뒤로 보냄
        s.append(s.popleft())


    return answer