def solution(arrayA, arrayB):
    gcd_a = gcd_of_arr(arrayA)
    gcd_b = gcd_of_arr(arrayB)

    for num in arrayB:
        if num % gcd_a == 0:
            gcd_a = 0
            break

    for num in arrayA:
        if num % gcd_b == 0:
            gcd_b = 0
            break

    return max(gcd_a, gcd_b)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def gcd_of_arr(arr):
    result = arr[0]

    for i in range(1, len(arr)):
        result = gcd(result, arr[i])

    return result