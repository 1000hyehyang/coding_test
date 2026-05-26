def can_make_min_distance(distance, rocks, n, min_dist):
    removed = 0
    prev = 0

    for rock in rocks:
        gap = rock - prev

        if gap < min_dist:
            removed += 1
        else:
            prev = rock

        if removed > n:
            return False

    return True


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    low = 1
    high = distance
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if can_make_min_distance(distance, rocks, n, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer