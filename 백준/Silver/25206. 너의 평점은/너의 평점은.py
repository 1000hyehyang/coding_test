# 등급별 과목평점 매핑
grade_points = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

# 총 학점과 총 점수 초기화
total_credits = 0
total_points = 0

# 20줄의 입력 처리
for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    
    # P 등급인 과목은 계산에서 제외
    if grade == 'P':
        continue
    
    # 학점과 과목평점의 곱을 누적
    total_credits += credit
    total_points += credit * grade_points[grade]

# 전공평점 계산 및 출력
if total_credits > 0:
    gpa = total_points / total_credits
    print(f"{gpa:.6f}")
else:
    print("0.000000")
