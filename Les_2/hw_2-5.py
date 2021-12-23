my_price = [57.8, 46.51, 97.43, 44.1, 63.55, 101.03, 74.86, 90.02, 14.52, 32.67]
b = my_price.sort()
i = 0
n = 0
my_list = []
while n < len(my_price):
    n += 1
    str_prices = ''.join(str(my_price[i]))
    a = str_prices.split('.')
    i += 1
    a = f'{a[0]} руб. {int(a[1]):0<2} коп.'
    my_list.append(a)
print(id(my_list), my_list)
my_list.reverse()
print(id(my_list), my_list)
print(f'Топ 5: {my_list[:5]}')
my_list.reverse()
print(f'Топ 5 по возрастанию: {my_list[5:]}')

