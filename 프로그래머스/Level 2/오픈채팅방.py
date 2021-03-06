"""
다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창을 만들기로 했다.
채팅방에 누가 들어오면
"[닉네임] 님이 들어왔습니다"
채팅방에서 누가 나가면
"[닉네임] 님이 나갔습니다"
가 출력된다
채팅방에서 닉네임을 변경하는 방법은 두가지 이다
1. 채팅방 나가고, 새로운 닉네임으로 다시 들어간다
2. 채팅방에서 닉네임을 변경한다.

닉네임 변경시에는 기존 채팅방에 출력된 메시지 닉네임도 전부 변경된다.
중복 닉네임을 허용한다.

채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 배개 변수로 주어질 떄,
모든 기록이 처리된후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return하도록
solution함수를 완성하라

제안 사항
record는 다음과 같은 문자열이 담긴 배열이며 , 1 이상 10만 이하
1. 모든 유저는 [유저아이디]로 구분
2. [유저아이디]사용자가 [닉네임]으로 입장시 "Enter [유저아이디][닉네임]
3. 퇴장시 "Leave [유저 아이디]
4. 변경시 "Change [유저 아이디][닉네임]

"""
from collections import defaultdict
def solution(record):
    dict_ = defaultdict()
    answer = []
    for i in record:
        info, id, *nick = i.split()
        if info in {"Enter", "Change"}:
            dict_[id] = nick[0]
    for i in record:
        info, id, *nick = i.split()
        if info == 'Enter':
            answer.append(f"{dict_[id]}님이 들어왔습니다.")
        if info == 'Leave':
            answer.append(f"{dict_[id]}님이 나갔습니다.")
    return answer