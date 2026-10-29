def solution(n):
    answer = 0
    i = 1
    while True:
        if bin(n).count('1') == bin(n + i).count('1'):
            answer = n + i
            break
        i += 1
        
    return answer