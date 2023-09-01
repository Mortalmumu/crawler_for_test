import requests
from bs4 import BeautifulSoup
#requests库可以帮助我们对网页发送请求
#BeautifulSoup库可以帮助我们解析requests库得到的html网页数据
url = "https://www.apple.com.cn"
#首先把要爬取的目标网站储存在变量url中
h = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'}
#有时目标网站会禁止爬虫程序访问，因此我们需要一个请求头来骗过目标网站，并把请求头存储在变量h里（字典形式）
#windows的请求头不长这个样子，并且每台电脑请求头都应该不同
response = requests.get(url,headers=h)
#设置变量名response来获取目标网页数据
#使用方法get，并传入目标网址，并放入请求头
html_test = response.text
#设置变量html_test来存储目标网页数据的text
soup = BeautifulSoup(html_test,"html.parser")
#设置变量名soup，并使用第二个库中的beautifulSoup库，传入实参（之前的变量名）
#第二个实参传入html.parser解释器
all_href = soup.find_all('a')
#设置一个变量名用来存储一个列表（因为find_all方法会返回一个可迭代对象）
#这里的'a'代表在text中寻找所有a标签
for href in all_href:
    print(href)
#这是一个简单的for循环，用于print出所有href