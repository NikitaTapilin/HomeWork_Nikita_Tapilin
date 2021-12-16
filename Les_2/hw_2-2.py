weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather = []
a = '"'
i = 0
n = 0
for i in weather_list:
    if weather_list[n].isdigit():
        weather.append(a)
        weather.append(weather_list[n].zfill(2))
        weather.append(a)
    elif weather_list[n][0] == '+':
        weather.append(a)
        weather.append(weather_list[n][:1] + weather_list[n][1:].zfill(2))
        weather.append(a)
    else:
        weather.append(weather_list[n])
    n += 1
print(weather)
print(' '.join(weather))
