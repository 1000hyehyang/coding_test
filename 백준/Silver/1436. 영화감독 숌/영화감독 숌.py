# 666이 연속으로 나오는 N번째 수
import sys

input = sys.stdin.readline
n = int(input())

count = 0
i = 0

while count < n:
    if '666' in str(i):
        count += 1
    i += 1

print(i - 1)