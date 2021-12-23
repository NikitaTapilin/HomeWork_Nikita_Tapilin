
for i in range(100):
    i += 1
    if i % 10 == 1 and i != 11:
        print(i, "процент")
    elif 1 < i % 10 < 5 and i != 12 and i != 13 and i != 14:
        print(i, "процента")
    else:
        print (i, "процентов")
