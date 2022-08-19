import requests

real = float(input('Quanto você deseja converter em real: '))
moeda = input('Para qual moeda quer converter (d para dollar, ou e para euro): ')
dindin = 1

if moeda == 'e':
    res = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-BRL")
    print(res)
    res_json = res.json()
    cotac_eur = float(res_json["EURBRL"]["bid"])
    dindin = real / cotac_eur
    print(f"Isso vale {dindin} euros.")

elif moeda == 'd':
    res = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    print(res)
    res_json = res.json()
    cotac_dolar = float(res_json["USDBRL"]["bid"])
    dindin = real / cotac_dolar
    print(f"Isso vale {dindin} dolares")
