rev = int(input('Введите объем выручки: '))
costs= int(input('Введите объем издержек: '))
per = int(input('Введите количесвот сотрудников: '))
prof= None
prof_1= None
if rev > costs:
    prof= (rev-costs)/rev
    print(prof)
    prof_1=(rev-costs)/per
    print(prof_1)
else:
    print("Убыток")
