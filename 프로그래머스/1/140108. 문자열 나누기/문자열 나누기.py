def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        if len(s) > 1:
            idx = 1
        else:
            answer += 1
            break
        x_cnt = 1
        x_no_cnt = 0
        
        while x_cnt != x_no_cnt:
            
            if s[idx] != x:
                x_no_cnt += 1
            else:
                x_cnt += 1
            
            idx += 1
            
            if idx >= len(s):
                break
            
        answer += 1
        s = s[x_cnt + x_no_cnt:]
        
    return answer