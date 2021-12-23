def thesaurus(*names):
    """Функция возвращает список в виде словаря с ключами первых букв значений."""
    all_names = {}
    for name in names:
        key = name[0]
        if key not in all_names:
            all_names[key] = []
        all_names[key].append(name)
    print(all_names)


thesaurus("Иван", "Мария", "Петр", "Илья")
