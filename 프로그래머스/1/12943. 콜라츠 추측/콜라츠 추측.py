def solution(num):
    answer = 0
    cnt = 0
    
    if num == 1:
        return 0
    
    while num != 1:
        if cnt == 500:
            return -1
        
        if num % 2 == 0:
            num //= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1
        
        if num == 1:
            break
    
    answer = cnt 
    
    return answer