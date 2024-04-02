#!/user/bin/env python3
from bs4 import BeautifulSoup
import re
html = """
<ul>
    <li><a href="hoge.html">hoge</li>
    <li><a href="https://example.com/fuga">fuga*</li>
    <li><a href="https://example.com/foo">foo*</li>
    <li><a href="https://example.com/adahoge.html">ada</li>
</ul>
"""
soup = BeautifulSoup(html, 'html.parser')
href_reg = re.compile(r"^https://")
links = soup.find_all('a', href=href_reg)
for link in links:
    print(link["href"])
    print(link.text)
