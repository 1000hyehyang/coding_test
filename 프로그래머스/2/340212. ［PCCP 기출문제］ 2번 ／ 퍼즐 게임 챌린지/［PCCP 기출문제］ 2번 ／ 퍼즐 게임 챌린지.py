def solution(diffs, times, limit):
    def can_clear(level):
        total = 0

        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]

            if diff <= level:
                total += time_cur
            else:
                mistake = diff - level
                time_prev = times[i - 1]

                total += mistake * (time_cur + time_prev) + time_cur

            if total > limit:
                return False

        return total <= limit

    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_clear(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer