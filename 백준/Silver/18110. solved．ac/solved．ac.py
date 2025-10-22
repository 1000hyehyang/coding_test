# 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산
# 제외되는 사람의 수는 위, 아래에서 각각 반올림
# 계산된 평균도 정수로 반올림

import sys

input = sys.stdin.readline
n = int(input())
scores = [int(input()) for _ in range(n)]

if n == 0:
    print(0)
else:
    scores.sort()
    exclude = int(n * 0.15 + 0.5)
    if exclude == 0:
        re_scores = scores
    else:
        re_scores = scores[exclude:-exclude]
    
    avg = int((sum(re_scores) / len(re_scores)) + 0.5)
    print(avg)