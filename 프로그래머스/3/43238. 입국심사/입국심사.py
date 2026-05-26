def solution(n, times):
    times.sort()

    left = 1
    right = times[-1] * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer