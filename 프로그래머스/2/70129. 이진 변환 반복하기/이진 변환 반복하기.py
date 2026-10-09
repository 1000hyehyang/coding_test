def solution(s):
    answer = []
    trans_cnt = 0
    zero_cnt = 0

    while s != '1':
        zero_cnt += s.count('0')
        x = s.replace('0', '')
        c = len(x)
        s = binary(c)
        trans_cnt += 1

    answer = [trans_cnt, zero_cnt]

    return answer

def binary(n):
    result = ''

    while n > 0:
        result += str(n % 2)
        n //= 2

    result = result[::-1]

    return result