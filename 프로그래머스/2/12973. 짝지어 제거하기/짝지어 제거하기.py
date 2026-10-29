def solution(s):
    stack = []
    
    for ch in s:
        stack.append(ch)
        
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                del stack[-2:]
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
    

    return answer