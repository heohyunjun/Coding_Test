'''
자연수 n개로 이루어진 중복집합(multi set) 중에 다음 두 조건을 만족하면 최고의 집합임
1. 각 원소의 합이 S가 되는 수의 집합
2. 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합

예를 들어서 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합은
{ 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }중 원소의 곱이 최대인건 4, 5

'''
def solution(n, s):
    if n > s:
        return [-1]
    q, r = divmod(s, n)
    answer = [q] * n
    for i in range(r):
        answer[i]+=1


    return sorted(answer)