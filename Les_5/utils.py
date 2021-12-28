from requests import get, utils
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings).split('/Valute')


def currency_rates(args):
    i = 0
    money = {}
    for num in content:
        if i < len(content) - 1:
            money[content[i].split(">")[-8][:3]] = content[i].split(">")[-2][:7]
            i += 1
    print(money[args.upper()])


currency_rates(input("Введите нужную валюту:"))

