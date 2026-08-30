def solution(n):
    answer = 0
    three = []
    
    while n >= 1:
        print(n % 3)
        three.append(n % 3)
        n //= 3
    
    for idx, num in enumerate(three):
        answer += num * (3 ** (len(three) - idx - 1))
    
    return answer

