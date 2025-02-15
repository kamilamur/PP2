def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Введите n: "))

for num in countdown(n):
    print(num, end=" ")