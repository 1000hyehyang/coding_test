def solution(s):
    answer = True
    s = sorted(s, reverse = True)
    length = len(s)
    if length != 4 and length != 6:
        return False
    if s[0].isdigit() is False:
        return False

    return answer