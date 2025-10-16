# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
# 예를 들면 ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

def solution(words):
    answer = 0
    for word in words:
        if is_group_word(word):
            answer += 1
    return answer

def is_group_word(word):
    # 연속된 문자가 있는지 확인, 근데 하나만 나오는 건 괜찮, 그 대신 뒤에서 다시 나오면 안됨
    lst = []  # 이미 등장했던 문자들을 저장
    prev = ''  # 이전 문자
    
    for char in word:
        # 현재 문자가 이전 문자와 다르고, 이미 나온 적이 있다면 그룹 단어가 아님
        if char != prev:
            if char in lst:
                return False
            lst.append(char)
        prev = char
    
    return True

n = int(input())
words = [input() for _ in range(n)]

print(solution(words))