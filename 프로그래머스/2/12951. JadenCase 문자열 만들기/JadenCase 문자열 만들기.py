def solution(s):
    sentence = s.split(' ')

    for i in range(len(sentence)):
        sentence[i] = sentence[i].capitalize()

    return ' '.join(sentence)