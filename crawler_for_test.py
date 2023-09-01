import requests
from bs4 import BeautifulSoup
url = "https://www.apple.com.cn"
h = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'}
response = requests.get(url,headers=h)
#print(response.text)
html_test = response.text
soup = BeautifulSoup(html_test,"html.parser")
all_href = soup.find_all('a')
for href in all_href:
    print(href)
