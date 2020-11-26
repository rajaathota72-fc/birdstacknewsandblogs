# import libraries
from bs4 import BeautifulSoup
import urllib.request
urlpage =  'https://www.uipath.com/blog/'
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
blognames = soup.findAll('h4', attrs={'class':'art-title'})
bn_tolist = list(blognames)
titles = []
for i in range(len(bn_tolist)):
    x = str(bn_tolist[i])
    mbnls = x[198:]
    # mbnls2 = mbnls[-12:]
    mbnls_title = mbnls[:-12]
    titles.append(mbnls_title)
print(titles[1:])