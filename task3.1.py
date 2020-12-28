month = int(input('Введите мсяц в виде числа от 1 до 12'))
month_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 12 or month == 1 or month == 2:
    print(f'Этот месяц относится к времени года: {month_list[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'Этот месяц относится к времени года: {month_list[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'Этот месяц относится к времени года: {month_list[2]}')
else:
    print(f'Этот месяц относится к времени года: {month_list[3]}')
