print('Структура данных "Товары"')
name = input('Введите название товара: ')
price = int(input('Введите стоимость товара: '))
quantity = int(input('Введите количество товара: '))
measurement = input('Введите еденицу измерения товара: ')
product_tuple1 = (1, {'название': name, 'стоимость': price, 'количество': quantity, 'ед.измерения': measurement})
name2 = input('Введите название товара: ')
price2 = int(input('Введите стоимость товара: '))
quantity2 = int(input('Введите количество товара: '))
measurement2 = input('Введите еденицу измерения товара: ')
product_tuple2 = (2, {'название': name2, 'стоимость': price2, 'количество': quantity2, 'ед.измерения': measurement2})
print(product_tuple1)
print(product_tuple2)
product_dict = {'название': [name, name2],
                 'цена': [price, price2],
                 'количество': [quantity, quantity2],
                 'ед.измерения': [measurement, measurement2]}
print(product_dict)