def solution(t, p):
    lst = []
    answer = 0
    for i in range(len(t) - len(p) + 1):
        lst.append(int(t[i : i + len(p)]))
    print(lst)
    for i in lst:
        if i <= int(p):
            answer += 1
    return answer