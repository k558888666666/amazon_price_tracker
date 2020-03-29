import requests
from bs4 import BeautifulSoup as bs
import smtplib
import time

URL = 'https://www.amazon.com/-/zh_TW/dp/B07ZPKR714/ref=sr_1_1?dchild=1&keywords=iphone+11&qid=1585446003&sr=8-1'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup_content = bs(page.content, 'html.parser')
    soup_prettify = bs(soup_content.prettify(), "html.parser")

    #title = soup_prettify.find(id = "productTitle").get_text()
    price = soup_prettify.find(id = "priceblock_ourprice").get_text()
    coverted_price = float(price[3:6])

    if(coverted_price < 650):
        send_mail()

    print(coverted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('k558888666666@gmail.com', 'bfgwyzghfwcolbks')

    subject = "Price fell down!!!!!!"
    body = 'Check https://www.amazon.com/-/zh_TW/dp/B07ZPKR714/ref=sr_1_1?dchild=1&keywords=iphone+11&qid=1585446003&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'k558888666666@gmail.com',
        'abssp72888@yahoo.com.tw',
        msg
    )
    print('sent it ')
    server.quit()
    
while(True):
    check_price()
    time.sleep(60 * 60 * 24)