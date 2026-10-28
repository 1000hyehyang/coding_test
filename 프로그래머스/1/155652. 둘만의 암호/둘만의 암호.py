def solution(s, skip, index):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    answer = ''

    for ch in s:
        pos = alphabet.index(ch) # 초기 위치

        for _ in range(index):
            pos = (pos + 1) % 26

            while alphabet[pos] in skip:
                pos = (pos + 1) % 26

        answer += alphabet[pos]

    return answer