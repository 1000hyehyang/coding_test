# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=

text = input()
# ljes=njak 이면 6개 lj, e, s=, nj, a, k
# ddz=z= 이면 3개 d, dz=, z=

def solution(text):
    alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for i in alphabet:
        text = text.replace(i, 'a')
    
    answer = len(text)
    return answer

print(solution(text))