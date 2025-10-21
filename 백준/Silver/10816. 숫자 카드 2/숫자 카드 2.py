import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
number_card = list(map(int, input().split()))
m = int(input())
result_card = list(map(int, input().split()))

counter = Counter(number_card)

result = [counter[i] for i in result_card]

print(' '.join(map(str, result)))