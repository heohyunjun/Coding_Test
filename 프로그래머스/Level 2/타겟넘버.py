'''
문제
n개의 음이 아닌 정수들있는데 순서바꾸지 않고 더하거나 빼서 target넘버를 만들려고함
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있음.
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

'''
def solution(numbers, target):
    base_ = [0]
    for i in numbers:
        tmp = []
        for j in base_:

            # +, -
            tmp.append(j + i)
            tmp.append(j - 1)
        base_ = tmp
    return base_.count(target)