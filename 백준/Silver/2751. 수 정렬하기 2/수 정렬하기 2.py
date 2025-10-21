# N개의 수가 주어졌을 때 오름차순으로 정렬 
import sys

input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
for i in lst:
    print(i)