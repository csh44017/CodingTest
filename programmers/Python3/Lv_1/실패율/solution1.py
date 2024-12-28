def solution(N, stages):
    fail_rate = []
    user = len(stages)
    for stage_num in range(1, N+1):
        cnt = stages.count(stage_num)
        if cnt == 0:
            fail_rate.append(0)
        else:
            fail_rate.append(cnt/user)
            user -= cnt
    
    sorted_stage = sorted(range(1, N+1), key=lambda k: fail_rate[k-1], reverse=True)
    return sorted_stage
