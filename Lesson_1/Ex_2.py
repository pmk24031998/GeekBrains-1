a = int(input('Введите количество секунд: '))
sek = a % 60
if a // 60 > 0:
    min = a // 60
    if min > 0:
        h = min // 60
        min = min - h * 60
        print(h, ':', min, ':', sek)
    else:
        print(min, ':', sek)
else:
    print(sek)
