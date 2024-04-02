#!/user/bin/env python3
import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("USAGE : download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

url = f"https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId={regionNumber}"

text = req.urlopen(url).read()

print(text.decode('utf-8'))