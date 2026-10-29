def solution(k, tangerine):
    answer = 0
    dic = {}

    for item in tangerine:
        dic[item] = dic.get(item, 0) + 1

    counts = sorted(dic.values(), reverse=True)

    i = 0
    n = 0

    while n < k:
        n += counts[i]
        i += 1
        answer += 1

    return answer