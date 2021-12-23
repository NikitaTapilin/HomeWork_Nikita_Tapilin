time = int(input("Введите кол-во секунд: "))
min = 60
hour = 3600
day = 86400
if time < min: #Меньше минуты
    print (time, "секунд")
elif 59 < time < hour: # Меньше часа
    print (time // min, "мин. ", time % min, "сек." )
elif 3599 < time < day: # Меньше суток
    print (time // hour, "час.", time % hour // min, "мин.", time % hour % min, "сек." )
else:
    print (time // day, "дн.", time % day // hour, "час.", time % day % hour // min, "мин.", time % min, "сек.")