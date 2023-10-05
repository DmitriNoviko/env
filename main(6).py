'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import requests
from bs4 import BeautifulSoup
url = "https://www.nstu.ru/news?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
news = soup.find_all("div", class_="bottomLine")

a = []
for n in news:
    url = n.select("a")[1]["href"]
    id = int(url.split("=")[1])
    title = n.select("a")[1].text
    a.append({"id": id, "title": title})

url = "https://www.nstu.ru/news?page=2"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
news = soup.find_all("div", class_="bottomLine")

b = []
for n in news:
    url = n.select("a")[1]["href"]
    id = int(url.split("=")[1])
    title = n.select("a")[1].text
    b.append({"id": id, "title": title})

url = "https://www.nstu.ru/news?page=3"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
news = soup.find_all("div", class_="bottomLine")

c = []
for n in news:
    url = n.select("a")[1]["href"]
    id = int(url.split("=")[1])
    title = n.select("a")[1].text
    c.append({"id": id, "title": title})


print(a)
print(b)
print(c)
