'''
양의 정수 x에 대한 함수 f(x) : x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
정수들이 담긴 배열 numbers가 매개변수로 주어집니다.
numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return
'''


def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:  # 짝수 일때
            binary_num = list(bin(number)[2:])
            binary_num[-1] = "1"
        else:  # 홀수 일때
            binary_num = bin(number)[2:]
            binary_num = "0" + binary_num
            one_idx = binary_num.rfind("0")
            binary_num = list(binary_num)
            binary_num[one_idx] = "1"
            binary_num[one_idx + 1] = "0"
        ans_num = int("".join(binary_num), 2)
        answer.append(ans_num)

    return answer