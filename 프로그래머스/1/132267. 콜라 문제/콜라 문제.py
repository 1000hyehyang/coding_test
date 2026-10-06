def solution(a, b, n):
    answer = 0

    while n >= a:
        get_bottle = (n // a) * b
        answer += get_bottle

        n = (n % a) + get_bottle

    return answer