def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        for sound in sounds:
            if sound * 2 in bab:
                break
        else:
            for sound in sounds:
                bab = bab.replace(sound, " ")

            if bab.strip() == "":
                answer += 1

    return answer