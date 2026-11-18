cnt = 0

while True:
    n = int(input())
    if n % 2 != 0:
        continue
    else:
        n //= 2
        print(n)
        cnt += 1
    
    if cnt == 3:
        break