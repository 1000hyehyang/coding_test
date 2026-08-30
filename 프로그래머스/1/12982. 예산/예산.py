def solution(d, budget):
    answer = 0
    money = 0
    d.sort()
    for i in d:
        if money + i <= budget:
            answer += 1
            money += i
    return answer