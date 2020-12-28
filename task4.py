words = input('Введите нескольок слов через пробел: ')
words_list = words.split()
for i, word in enumerate(words_list, start=1):
    print(i, word[:10])