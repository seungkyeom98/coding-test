def solution(skill, skill_trees):
    count = 0
    
    for tree in skill_trees:
        skill_order = "".join([s for s in tree if s in skill])  # skill에 포함된 문자만 추출
        
        if skill_order == skill[:len(skill_order)]:  # skill의 순서를 유지하는지 확인
            count += 1
    
    return count
