def move(r, c, target_r, target_c):
    if r < target_r:
        r += 1
    elif r > target_r:
        r -= 1
    elif c < target_c:
        c += 1
    elif c > target_c:
        c -= 1

    return r, c


def solution(points, routes):
    active = []

    # 모든 로봇의 초기 위치 설정
    # routes[0] -> [4, 2] 1번째 로봇이 4 포인트에서 2 포인트로 이동한다는 뜻.
    # 즉, points[route의 내부 값 - 1]이 초기 로봇의 위치.
    for route in routes:
        r, c = points[route[0] - 1]
        active.append([r, c, 1, route])

    answer = 0

    while active:
        # 1. 현재 시간의 충돌 검사
        counts = {}

        for r, c, idx, route in active:
            pos = (r, c)
            counts[pos] = counts.get(pos, 0) + 1

        for count in counts.values():
            if count >= 2:
                answer += 1

        # 2. 운송 완료 로봇 제외 및 나머지 이동
        next_active = []

        for r, c, idx, route in active:
            if idx == len(route):
                continue

            target_r, target_c = points[route[idx] - 1]

            r, c = move(r, c, target_r, target_c)

            if (r, c) == (target_r, target_c):
                idx += 1

            next_active.append([r, c, idx, route])

        active = next_active

    return answer