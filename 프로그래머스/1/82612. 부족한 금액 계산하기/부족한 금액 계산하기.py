def solution(price, money, count):
    need = 0
    
    for i in range(count):
        need += price * (i + 1)
    
    answer = need - money
    
    if answer <= 0:
        answer = 0
    
    return answer