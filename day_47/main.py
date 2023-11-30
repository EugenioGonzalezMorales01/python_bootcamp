import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

amazon_link = 'https://www.amazon.com.mx/Nuevos-Apple-AirPods-Tercera-generaci%C3%B3n/dp/B09JQL3NWT/ref=sr_1_6' \
              '?keywords=airpods+pro&qid=1688272922&sprefix=air+pods%2Caps%2C139&sr=8-6'
headers = {
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.67',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-ch-ua-platform': 'Windows',
    'X-Forwarded-For': '189.190.49.85',
    'x-forwarded-proto': 'https',
    'x-https': 'on'
}
response = requests.get(amazon_link, headers=headers)
response = response.text

sp = BeautifulSoup(response, 'lxml')
price = sp.select_one('span.a-offscreen')
price = float(price.text.split("$")[1].replace(",",""))
print(price)

if price < 7500:

    app_psw = 'mdrfzrhhuycdfxzr'
    email = 'eugenio.de.astora@gmail.com'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=email, password=app_psw)
        connection.sendmail(from_addr=email, to_addrs='eugenio.g.m@outlook.es', msg=f'Subject:Price Drop!\n\nPrice of Airpods (3th gen) has drop to {price}\nBuy it here: {amazon_link}')
