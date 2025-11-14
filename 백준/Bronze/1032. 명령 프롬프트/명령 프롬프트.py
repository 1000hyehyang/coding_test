import sys
input = sys.stdin.readline
n = int(input())

data_list = [input().rstrip() for _ in range(n)]

# 문자 비교해서 다르기만 하면 ?임 

standard = list(data_list[0])

for data in data_list:
    for j in range(len(data)):
        if data[j] != standard[j]:
            standard[j] = '?'

print(''.join(standard))