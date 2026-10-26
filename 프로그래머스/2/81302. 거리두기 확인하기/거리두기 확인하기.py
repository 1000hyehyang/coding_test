from itertools import combinations

def solution(places):
    answer = []

    for place in places:
        people = []
        
        for r, row in enumerate(place):
            for c, seat in enumerate(row):
                if seat == 'P':
                    people.append((r, c))

        valid = 1

        for (r1, c1), (r2, c2) in combinations(people, 2):
            dist = abs(r1 - r2) + abs(c1 - c2)

            if dist > 2:
                continue

            if dist == 1:
                valid = 0
                break

            # 맨해튼 거리가 2인 경우
            if r1 == r2: # 같은 행에 있는 경우
                if place[r1][(c1 + c2) // 2] != 'X':
                    valid = 0
                    break

            elif c1 == c2: # 같은 열에 있는 경우
                if place[(r1 + r2) // 2][c1] != 'X':
                    valid = 0
                    break

            else:
                if place[r1][c2] != 'X' or place[r2][c1] != 'X':
                    valid = 0
                    break

        answer.append(valid)

    return answer