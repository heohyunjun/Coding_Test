'''
구명보트

1. 구명보트는 작아서 한 번에 최대 2명씩 탈 수있음, 무게 제한도 있음
2. 예를 들어 사람무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트 무게 제한이 100kg라면
    2번쨰 4번째 사람은 같이 탈 수 있지만, 1번째 3번째 사람 무게합은 130이기 떄문에 불가능
3. 구명 보트를 최대한 적게 사용하여 모든 사람을 구출하려고 함
'''
def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1

    # 오름 차순 정렬
    people.sort()
    while start <= end:
        answer +=1

        # 작은놈, 큰놈 둘 다 태울수 있는 경우
        if people[start] + people[end] <= limit:
            start +=1
        # 둘다 못태우면 큰놈만 태움
        end -=1
    return answer