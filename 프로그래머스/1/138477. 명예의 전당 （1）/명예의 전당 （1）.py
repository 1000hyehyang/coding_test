def solution(k, score):
    answer = []
    hall_of_fame = []
    
    for i in range(len(score)):
        if len(hall_of_fame) < k:
            hall_of_fame.append(score[i])
            hall_of_fame.sort()
        else:
            if hall_of_fame[0] < score[i]:
                hall_of_fame.pop(0)
                hall_of_fame.append(score[i])
                hall_of_fame.sort()
                
        answer.append(hall_of_fame[0])
                
    return answer