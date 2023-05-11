# ЗАДАНИЕ 13.8.19 (HW-03)
n = int(input('Введите количество билетов: '))
summa = 0
for ticket in range(1, n+1):
    age = int(input(f'Введите возраст для {ticket} билета из {n}: '))
    if 18 <= age <= 25:
        summa += 990
    elif 25 < age:
        summa += 1390
print('Сумма без скидки: ', summa)
summa = summa - summa * 0.1 if n > 3 else summa
print('Сумма со скидкой: ', summa)
