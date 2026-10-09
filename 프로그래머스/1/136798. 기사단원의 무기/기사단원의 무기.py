def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        count = divisor(i)

        if count > limit:
            answer += power
        else:
            answer += count

    return answer


def divisor(n):
    count = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2

    return count