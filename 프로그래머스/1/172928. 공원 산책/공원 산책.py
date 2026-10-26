def solution(park, routes):
    # 1. 공원의 크기
    h = len(park)
    w = len(park[0])

    # 2. 시작 위치 찾기
    for i, row in enumerate(park):
        if 'S' in row:
            x = i
            y = row.index('S')
            break

    # 3. 방향별 이동 값
    directions = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }

    # 4. 명령 순서대로 실행
    for route in routes:
        op, n = route.split()
        n = int(n)

        dx, dy = directions[op]

        # 실제 위치는 유지하고 임시 위치로 검사
        nx, ny = x, y
        valid = True

        # n칸 이동 가능한지 확인
        for _ in range(n):
            nx += dx
            ny += dy

            # 공원 밖으로 나가는 경우
            if not (0 <= nx < h and 0 <= ny < w):
                valid = False
                break

            # 장애물을 만난 경우
            if park[nx][ny] == 'X':
                valid = False
                break

        # 모든 이동이 가능할 때만 실제 위치 변경
        if valid:
            x, y = nx, ny

    return [x, y]