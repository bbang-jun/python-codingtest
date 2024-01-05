def solution(N, stages):
    answer = []
    # 각 stage에 존재하는 사람
    stage_person = [0] * (N+2)
    # 사용자를 줄여나가기 위한 리스트
    total = len(stages)
    # 각 stage에서의 실패율
    # fault_rate = [0] * (N+1)
    fault_rate = {}
    
    for i in stages:
        if i <= N:
            stage_person[i]+=1 
    
    for i in range(1, N+1):
        if total != 0:
            fault_rate[i] = stage_person[i] / total
            total -= stage_person[i]
        else:
            fault_rate[i] = 0
    
    answer = sorted(fault_rate, key=lambda x: fault_rate[x], reverse=True)
    
    
    
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 
    return answer