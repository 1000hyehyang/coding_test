def solution(sizes):
    answer = 0
# 50 60 / 30 70 / 30 60 / 40 80
    for i in sizes:
        i.sort()
    w, h = 0, 0
    
    for x in sizes:
        if x[0] < w and x[1] < h:
            continue
        if x[0] >= w:
            w = x[0]
        if x[1] >= h:
            h = x[1]
    
    answer = w * h
        
    return answer
