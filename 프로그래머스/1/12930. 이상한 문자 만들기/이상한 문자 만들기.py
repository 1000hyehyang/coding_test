def solution(s):
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            idx = 0
            continue
            
        if idx % 2 == 0:
            answer += s[i].upper()
            idx += 1
        else:
            answer += s[i].lower()
            idx += 1
    return answer