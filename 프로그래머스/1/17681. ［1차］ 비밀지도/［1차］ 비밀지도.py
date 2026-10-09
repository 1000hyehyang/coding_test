def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        result = ''
        for x, y in zip(decoding(arr1[i], n), decoding(arr2[i], n)):
            if x == '1' or y == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
        
    return answer

def decoding(n, length):
    result = ''

    while n > 0:
        result = str(n % 2) + result
        n //= 2
    
    while len(result) < length:
        result = '0' + result
    
    return result
    