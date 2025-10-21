import sys

input = sys.stdin.readline
n = int(input()) # 참가자 수
applicants = map(int, input().split()) # 티셔츠 사이즈 별 신청자 수 S, M, L, XL, XXL
t, p = map(int, input().split()) # 티셔츠와 펜의 묶음 수

# 23
# 3 1 4 1 5 9
# 5 7

# 총 23명이고 티셔츠는 5묶음으로만 파니까, 9명의 신청자가 있는 XXL 때문에 XXL 티셔츠는 2묶음을 사야함.
# 따라서 티셔츠는 총 1 + 1 + 1 + 1 + 1 + 2 = 7묶음을 사야함.
# applicants를 하나씩 돌면서 applicants[i] <= t 이면 1묶음, 아니면 (appicants[i] / t + 1) 묶음 
# 펜은 남으면 안되니까 23명이 7개가 들어있는 묶음 3개를 사고 2자루를 더 사야함.
# 펜은 n / p 묶음 + n % p 자루를 사야함.

total_t = 0
for applicant in applicants:
    if applicant == 0:
        continue
    elif applicant % t == 0:
        total_t += applicant // t
    else:
        total_t += applicant // t + 1

total_p = int(n / p)
individual_p = n % p

print(total_t)
print(total_p, individual_p)