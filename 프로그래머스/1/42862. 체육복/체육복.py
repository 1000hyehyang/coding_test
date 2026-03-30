def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
            
    new_lost = []
    for x in lost:
        if x in reserve:
            reserve.remove(x)
        else:
            new_lost.append(x)

    lost = new_lost
    
    for i in lost:
        if (i - 1) in reserve:
            reserve.remove(i - 1)
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
        else:
            n -= 1
            
    answer = n
    return answer