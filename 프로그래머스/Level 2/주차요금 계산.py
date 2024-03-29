'''
요금표, 차량의 입/출차 기록이 주어질때 차량별 주차 요금을 계산하려고함
- 어떤 차량의 입차 후 출차 기록이 없으면, 23:59분에 출차
- 누적 주차 시간이 기본시간 이하면, 기본요금 청구
- 누적 주차 시간이 기본 시간을 초과하면, 기본요금에 더해서, 초과한 시간에 대해서
    단위 시간 마다 단위 요금 청구
- 초과한 시간이 단위 시간으로 나누어 떨이지지 않으면, 올림
- [a] : a보다 작지 않은 최소의 정수를 의미, 즉 올림을 의미

'''