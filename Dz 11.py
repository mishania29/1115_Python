import requests

responce = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

valuta_list = []
responce_text = responce.text.split('<td class="value-name" data-label="Назва валюти">')
for elem in responce_text:
    if elem.startswith("$"):
        for elem2 in elem.split('<td class="value-name" data-label="Назва валюти">'):
            if elem2.startswith("$"):
                valuta_list.append(float(elem2.replace("$", "").replace(",", "")))

print("Доллар до гривні -", valuta_list[0])