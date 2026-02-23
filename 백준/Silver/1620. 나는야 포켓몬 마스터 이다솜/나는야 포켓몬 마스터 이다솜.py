n, m = map(int, input().split())

pokemon = []
name_dict = {}

for i in range(n):
    name = input()
    pokemon.append(name)
    name_dict[name] = i + 1

for _ in range(m):
    question = input()
    if question.isdigit():
        print(pokemon[int(question) - 1])
    else:
        print(name_dict[question])