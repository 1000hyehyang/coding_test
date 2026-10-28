def solution(lottos, win_nums):
    matching = [6, 6, 5, 4, 3, 2, 1] # 인덱스가 일치 개수, 값이 순위
    
    lottos.sort()
    win_nums.sort()
    
    cnt_match = 0
    cnt_zero = 0
    
    for i in range(6):
        if lottos[i] in win_nums:
            cnt_match += 1
        elif lottos[i] == 0:
            cnt_zero += 1
    
    max_rank = matching[cnt_match + cnt_zero]
    min_rank = matching[cnt_match]
    
    answer = [max_rank, min_rank]
    
    
    return answer