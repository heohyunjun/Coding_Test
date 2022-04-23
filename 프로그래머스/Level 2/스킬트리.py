'''
스킬 트리
선행 스킬 순서대로 스킬을 배울 수 있고, 다른 스킬들은 순서 상관없이 배울 수 있음
선행 스킬 순서 skill과 유저들이 만든 스킬트리를 담은 배열 skill_trees가 매개변수로 주어질 떄
가능한 스킬트리 개수를 return하는 solution 함수 작성

'''
# 방식 1
def solution(skill, skill_trees):
    answer = 0
    for s_tree in skill_trees:
        skill_list = list(skill)
        for s in s_tree:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer


# 방식 2
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer
