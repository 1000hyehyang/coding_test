name = [None, 'John', 'Tom', 'Paul', 'Sam']

for i in range(100):
    n = int(input())
    if 0 < n <= 4:
        print(name[n])
    else:
        print("Vacancy")
        break
    