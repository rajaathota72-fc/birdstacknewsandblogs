import requests
from bs4 import BeautifulSoup
url = "https://www.softomotive.com/blog-news-events/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []
for link in soup.find_all('a'):
    links =link.get('href')
    urls.append(links)
print(urls)
print(urls[49])