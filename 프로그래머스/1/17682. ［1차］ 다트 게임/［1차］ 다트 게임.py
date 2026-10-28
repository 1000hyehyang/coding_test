def solution(dartResult):
    # 무조건 3세트만 나오니까 세트별 점수를 저장하자.
    
    set_score = [dartResult[:2]]
    score_map = {'S' : 1, 'D' : 2, 'T' : 3}
    pointer = 0
    
    for i in dartResult[2:]:
        if i.isdigit():
            if i == '0' and set_score[pointer][-1].isdigit():
                set_score[pointer] += i
            else:
                pointer += 1
                set_score.append(i)
        else:
            set_score[pointer] += i
    
    print(set_score)
    set_result_temp = []
    
    for score in set_score:
        if len(score) == 2:
            set_result_temp.append(int(score[0]) ** score_map.get(score[1]))
        else:
            if score[1].isdigit():
                set_result_temp.append(int(score[:2]) ** score_map.get(score[2]))
            else:
                set_result_temp.append(int(score[0]) ** score_map.get(score[1]))
    
    print(set_result_temp)
    
    for idx, score in enumerate(set_score):
        if '*' in score:
            if idx == 0:
                set_result_temp[idx] *= 2
            else:
                set_result_temp[idx] *= 2
                set_result_temp[idx - 1] *= 2
        if '#' in score:
            set_result_temp[idx] *= -1
    
    answer = 0
    
    for result in set_result_temp:
        answer += result
    
    return answer