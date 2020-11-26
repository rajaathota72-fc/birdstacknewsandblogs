# import libraries
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import urljoin
def uipath_scrape():
    urlpage = 'https://www.uipath.com/blog/'
    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    blognames = soup.findAll('h4', attrs={'class': 'art-title'})
    bn_tolist = list(blognames)
    titles = []
    for i in range(len(bn_tolist)):
        x = str(bn_tolist[i])
        mbnls = x[198:]
        mbnls_title = mbnls[:-12]
        titles.append(mbnls_title)
    results_1 = titles[1:]
    return results_1
print(uipath_scrape())
def apicall_summary():
    result_2 = uipath_scrape()
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
    result_3 = result_2[0].replace(" ","-")
    path = urljoin("https://www.uipath.com/blog/",str(result_3))
    querystring = {"sentences": "5","url": path}
    headers = {
        'accept': "application/json",
        'x-rapidapi-key': "82f634005emsha418ca5ea3be960p110c9bjsn150bfa1b8522",
        'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_1 =response.json()
    response_2 = dict(response_1)
    return (path,response_2['summary'],"UIpath")
import streamlit as st
st.title("News Feed Summary Test - Admin Panel")
#st.image("RPAnews.png", width = 500)
st.sidebar.title("Choose the website to scrape")
st.sidebar.image("RPAnews.png",width = 300)
st.write("This is a test Admin Panel to scrape the websites for news on RPA and summarize them which can be later be part of metaportal in news and blog section")
checkbox = st.sidebar.selectbox("Select one or multiple",("dropdown to select","Uipath","RPA today","Automation Anywhere"))
if checkbox == "Uipath":
    display1 = uipath_scrape()
    st.success("Successfully scraped {} recent articles".format(len(display1)))
if st.button("get Summary sample"):
    display2 = apicall_summary()
    st.success("Url = {}".format(display2[0]))
    st.success("summary = {}".format(display2[1]))
    st.success("source = {}".format(display2[2]))