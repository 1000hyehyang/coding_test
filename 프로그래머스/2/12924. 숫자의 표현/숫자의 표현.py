def solution(n):
    answer = 0
    num = 1
    
    while num <= n:
        total = 0
        i = num
        
        while total <= n:
            total += i
            
            if total == n:
                answer += 1
                break
            
            i += 1
        
        num += 1
    
    return answer