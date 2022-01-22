# -*- coding: utf-8 -*-
"""

# 피보나치수

- 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

- 예를들어

 - F(2) = F(0) + F(1) = 0 + 1 = 1

 - F(3) = F(1) + F(2) = 1 + 1 = 2

 - F(4) = F(2) + F(3) = 1 + 2 = 3

 - F(5) = F(3) + F(4) = 2 + 3 = 5
"""

n = 3

def fibo(n):
    sum = 0
    f0

def solution(n):
    fibo = []
    for num in range(0, n+1):
        if num == 0:
            fibo.append(0)
        elif num == 1:
            fibo.append(1)
            
        else:
            print(fibo)
            fibo.append(fibo[num - 2] + fibo[num - 1])

    return fibo[n] % 1234567

def solution(n):
    a,b = 0,1
    for i in range(n):
        print(a,b)
        a,b = b,a+b
        print(a,b)
        print("=====")
    return a

def solution(n):
    fib = [0, 1, 1]
    for i in range(3, n + 1):
        fib.append((fib[i-2] + fib[i-1]) % 1234567)
    return fib[-1]

def solution(n):
    fibo = [0, 1, 1]
    for i in range(3, n +1):
        fibo.append(fibo[i-2] + fibo[i-1])
    return fibo[-1] %1234567

