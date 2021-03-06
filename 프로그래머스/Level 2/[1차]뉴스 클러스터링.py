'''
여러 언론사의 속보성 뉴스를 보면 비슷비슷한 제목의 기시떄문에 필요한 기사를 찾기 어려움
다음 뉴스 개발 업무를 맡게 된 튜브는 편리하게 뉴스를 찾아볼 수 있도록하는 업무를 맡음
개발 방향성을 잡기 위해 "카카오 신입 개발자 공채" 관련 기사를 검색해봄
- 카카오 첫 공채..'블라인드' 방식 채용
- 카카오, 합병 후 첫 공채.. 블라인드 전형으로 개발자 채용
- 카카오, 블라인드 전형으로 신입 개발자 공채
- 카카오 공채, 신입 개발자 코딩 능력만 본다
- 카카오, 신입 공채.. "코딩 실력만 본다"
- 카카오 "코딩 능력만으로 2018 신입 개발자 뽑는다"
기사의 제목을 기준으로 "블라인드 전형"에 주목하는 기사와 "코딩 테스트"에 주목하는 기사로 나뉘는 걸 알 수 있음
튜브는 이들을 각각 묶어서 보여주면 카카오 공채 관련 기사를 찾아보는 사용자에게 유용용

자카드 유사도를 사용할 것
자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중 하나
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 듀 집합의 교집합 크기를 두 집합의 합집합의 크기로 나눈 값

예를 들어 A = {1, 2, 3}, B = {2,3,4}라고 할떄 , A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}
집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다
자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있음
다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면,
교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로,
자카드 유사도 J(A, B) = 3/7, 약 0.42
이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다. 문자열 "FRANCE"와 "FRENCH"가 주어졌을 때,
이를 두 글자씩 끊어서 다중집합을 만들 수 있다.
각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며,
교집합은 {FR, NC},
합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로,
두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH")
'''

from collections import Counter
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_list, str2_list = [], []

    for idx in range(len(str1) -1):
        if str1[idx :idx+2].isalpha():
            str1_list.append(str1[idx :idx+2])

    for idx in range(len(str2) -1):
        if str2[idx :idx+2].isalpha():
            str2_list.append(str2[idx :idx+2])

    cnt1, cnt2 = Counter(str1_list), Counter(str2_list)

    intersaction_ = list((cnt1 & cnt2).elements())
    union_ = list((cnt1 | cnt2).elements())
    if len(intersaction_) == 0and len(union_)  == 0:
        return 65536
    else:
        return int(len(intersaction_)/len(union_) * 65536)