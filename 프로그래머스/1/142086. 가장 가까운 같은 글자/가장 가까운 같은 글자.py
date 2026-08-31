def solution(s):
    answer = []
    lst = []
    
    for i in s:
        if i not in lst:
            answer.append(-1)
            lst.append(i)
        else:
            lst.append(i)
            count = []
            for j in range(len(lst) - 1):
                if lst[j] == i:
                    count.append(len(lst) - 1 - j)
            answer.append(min(count))
    return answer