import requests
from bs4 import BeautifulSoup
import time
import smtplib

URL = "https://www.amazon.com/Apple-AirPods-Wireless-Charging-Latest/dp/B07PYLT6DN"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0"}
WANTED_PRICE = 150
EMAIL_ADDRESS = "seanpmcg99@gmail.com"


def trackPrice():
    price = int(getPrice())
    if price > WANTED_PRICE:
        diff = price - WANTED_PRICE
        print(f"It's still {diff} too expensive")
    else:
        print("Cheaper!!")
        sendMail()


def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()[1:4]
    print(title)
    print(price)
    return price

def sendMail():
    subject = "Amazon Price has Dropped!"
    mailtext = "Subject:"+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, "Ballincurry1925")
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print("Sent Email")
    pass

if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(60)