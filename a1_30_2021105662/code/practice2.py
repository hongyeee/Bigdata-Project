#!/user/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'xml')
    data = soup.find_all("location")
    
    for location in data:
        print('[ '+location.find("tmEf").text+" ] "+ location.find("city").text + "\t"+ location.find("wf").text)


if __name__ == "__main__":
    main()