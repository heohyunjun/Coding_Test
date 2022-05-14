'''
x의 모든 0을 제거
x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return
'''

def solution(s):
    step = 0
    cnt = 0
    while True:
        if s == '1':
            break
        else:
            cnt += s.count('0')
            s = bin(len(s.replace('0', '')))[2:]
            step += 1

    return [step, cnt]