N, a = map(int,input().split())
cnt = 1
while cnt <= N:
    if cnt % a == 0:
        print(1)
    else:
        print(0)
    
    cnt += 1