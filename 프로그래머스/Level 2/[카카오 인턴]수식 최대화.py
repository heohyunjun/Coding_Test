'''
해커톤 대회에 참가하는 모든 참가자들에게는 숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식이 전달되며,
가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하는 것
단, 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 합니다. 즉, + > - > * 또는 - > * > + 등과 같이 연산자 우선순위를 정의할 수 있으나
 +,* > - 또는 * > +,-처럼 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없음
참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 우승 시 받을 수 있는 가장 큰 상금 금액을 return
'''

from itertools import permutations

def calc(op, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if op[seq] == "*":
            split_data = exp.split("*")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("*".join(temp)))

        if op[seq] == "+":
            split_data = exp.split("+")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("+".join(temp)))

        if op[seq] == "-":
            split_data = exp.split("-")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("-".join(temp)))

def solution(expression):
    answer = 0
    operations = list(permutations(['*', '+', '-'], 3))

    for op in operations:
        result = abs(int(calc(op, 0, expression)))

        if result > answer:
            answer = result

    return answer