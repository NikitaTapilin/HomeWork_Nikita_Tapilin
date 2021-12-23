def num_translate(num):
    """Функция возвращает перевод числительного"""
    my_dict_1 = {
        'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
        'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
        'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
    }
    print(f'"{my_dict_1[num]}"')


num_translate('six')
