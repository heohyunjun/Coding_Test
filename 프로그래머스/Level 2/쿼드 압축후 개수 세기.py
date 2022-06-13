'''
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr
당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하며 구체적인 방식은 다음과 같음

당신이 압축하고자 하는 특정 영역을 S라고 정의
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축
그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤,
각 정사각형 영역에 대해 같은 방식의 압축을 시도
arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때,
배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return
'''
def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return
        answer[init] += 1
    comp(0, 0, N)
    return answer