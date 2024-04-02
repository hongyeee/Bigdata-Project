#!/user/bin/env python3
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
import datetime

url = "https://finance.naver.com/marketindex/"
webpage = req.urlopen(url).read()
soup = BeautifulSoup(webpage, "html.parser")
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
price = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print("DATE: " + now + " 미국 USD : " + price.string)