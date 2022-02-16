rev = int(input('Введите объем выручки: '))
costs= int(input('Введите объем издержек: '))
if rev > costs:
    print('Прибыль')
elif rev== costs:
    print('Так себе поработли')
else:
    print('Убыток')