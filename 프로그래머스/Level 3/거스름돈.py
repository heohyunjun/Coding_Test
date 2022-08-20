'''
Finn은 소님들꼐 거스름돈을 n월 줄 때 방법의 경우의 수를 구하려고함
5원을 거슬러줘야하고 , 1 2 5원이 있다면 4가지 방법이 있음

거슬러 줘야 하는 금액 n과 Finn이 현재 보유하고 있는 돈의 종류가 money 매개변수로 주어 질 때,
n원을 거슬러 줄 방법의 수를 return
'''
def solution(n, money):
    rest = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            if i >= m:
                rest[i] += rest[i-m]

    return rest[n] % 1000000007