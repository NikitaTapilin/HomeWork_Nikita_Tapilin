from random import choice


# Первое решение без удаления слов:
def get_jokes(n):
    """Получаем заданное кол-во рандомно сформированных шуток из списков"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    while i < n:
        random_words = f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"'
        print(random_words)
        i += 1


get_jokes(3)

print('*' * 30)


# Второе решение с удалнием слов из списков:
def get_jokes(n):
    """Получаем заданное кол-во (<5) шуток рандомно сформированных слов из списков,
    c последующим исключением их из списка"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    while i < n:
        i += 1
        random_noun = choice(nouns)
        nouns.remove(random_noun)
        random_adverb = choice(adverbs)
        adverbs.remove(random_adverb)
        random_adjective = choice(adjectives)
        adjectives.remove(random_adjective)
        print(f'"{random_noun} {random_adverb} {random_adjective}"')


get_jokes(4)
