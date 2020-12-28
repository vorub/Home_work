my_list = [11, 8, 7, 6, 1]
print(f'Рейтинг:\n{my_list}')
new_rating = int(input('Введите новый элемент рейтинга: '))
my_list.append(new_rating)
my_list.sort(reverse=True)
print(f'Новый рейтинг:\n{my_list}')
