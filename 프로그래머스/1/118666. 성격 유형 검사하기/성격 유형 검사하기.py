def solution(survey, choices):
    answer = ''
    # survey에서 첫번째는 비동의 관련, 두 번째는 동의 관련
    agree_map = [0, 3, 2, 1, 0, 1, 2, 3] # choice 번호대로 점수 부여
    
    score = {
    'R': 0,
    'T': 0,
    'C': 0,
    'F': 0,
    'J': 0,
    'M': 0,
    'A': 0,
    'N': 0
    }
    
    for idx, choice in enumerate(choices):
        if choice > 4: # 동의
            score[(survey[idx][1])] += agree_map[choice]
        elif choice < 4: # 비동의
            score[(survey[idx][0])] += agree_map[choice]
    
    print(list(score.keys())[0])
    
    for i in range(0, 8, 2):
        if list(score.values())[i] >= list(score.values())[i + 1]:
            answer += list(score.keys())[i]
        elif list(score.values())[i] < list(score.values())[i + 1]:
            answer += list(score.keys())[i + 1]
    
    return answer