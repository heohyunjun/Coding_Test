'''
다른 개발자가 작성한 소스코드를 분석하여 문제점을 발견하고 수정해야하는 업무
소스 코든 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나고 있음
'(', ')'로만 이루어진 문자열이 있을 경우, '(', ')'의 개수가 같다면 균형잡힌 괄호 문자열
추가로 여기에 '(', ')'의 짝도 모두 맞을 경우네는 올바른 괄호 문자열이라고 부름
'(' 와 ')' 로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열" 이라면 다음과 같은 과정을 통해 "올바른 괄호 문자열"로 변환할 수 있음
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
'''
def solution(p):
    answer = ''
    if correct(p):
        return p
    answer = change(p)
    return answer

def separate(p):
    l, r = 0, 0
    for idx in range(len(p)):
        if p[idx] =='(':
            l+=1
        else:
            r+=1
        if l==r:
            u = p[:idx+1]
            v = p[idx+1:] if idx+1 < len(p) else ""
            break
    return u, v

def correct(p):
    stack = []
    for char in p:
        if char =='(':
            stack.append(char)
        else:
            if not len(stack):
                return False
            elif stack[-1] == '(':
                stack.pop()
    return False if len(stack) else True

def change(p):
    result = ""
    if not len(p):
        return ""
    u, v = separate(p)
    if correct(u):
        result =  u+change(v)
    else:
        tmp ='('
        tmp += change(v)
        tmp+=')'
        u =u[1:-1]
        for char in u:
            if char =='(':
                tmp+=')'
            else:
                tmp+='('
        result +=tmp
    return result
