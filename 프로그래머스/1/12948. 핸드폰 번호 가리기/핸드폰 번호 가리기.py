def solution(phone_number):
    length = len(phone_number)
    star = '*' * (length - 4)
    answer = f'{star}{phone_number[length - 4:]}'
    return answer