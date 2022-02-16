a = int(input("Введите число: "))
n = 0
m = 0
while a // 10 > 0:
    m = a % 10
    if m > n:
        n = m
    a = a // 10
print(n)
