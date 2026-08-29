def solution(s):
    length = len(s)
    answer = ''
    
    if length % 2 == 0:
        answer = f"{s[length // 2 - 1 : length // 2 + 1]}"
    else:
        answer = f"{s[length // 2]}"

    return answer