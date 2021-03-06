'''
양의 정수 n이 주어짐, 이 숫자를 k진수로 바꿧을 때, 변환된 수 안에 아래 조건에 맞는 소수가 몇 개인지 체크
- 0P0처럼 소수 양쪽에 0이 있는 경우
- P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
- 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
- P처럼 소수 양쪽에 아무것도 없는 경우
- 단, P는 각 자릿수에 0을 포함하지 않는 소수
    - 예를 들어, 101은 P가 될 수 없음
정수 n과 k가 매개변수로 주어집니다.
n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return
'''
import math
def is_prime(num):
    if num==1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def change(n, k):
    ret = ''
    while n>0:
        n, mod = divmod(n, k)
        ret+=str(mod)
    return ret[::-1]

def solution(n, k):
    answer = 0
    change_num = change(n, k)
    for i in change_num.split('0'):
        if i.isdigit() and is_prime(int(i)):
            answer+=1
    return answer
