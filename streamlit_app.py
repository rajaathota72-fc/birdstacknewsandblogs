import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def choose_blog(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        links =link.get('href')
        urls.append(links)
    return urls
def apicall_summary(path):
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
    querystring = {"sentences": "5","url": path}
    headers = {
        'accept': "application/json",
        'x-rapidapi-key': "82f634005emsha418ca5ea3be960p110c9bjsn150bfa1b8522",
        'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_1 =response.json()
    response_2 = dict(response_1)
    return (path,response_2['summary'])
import streamlit as st
st.title("Birdstack News and Blogs - Inshorts")
#st.image("RPAnews.png", width = 500)
st.sidebar.title("Choose the Webpage")
st.sidebar.image("RPAnews.png",width = 300)
st.write("Select the website from where you want recent blog / News to be summarised")
checkbox = st.sidebar.selectbox("Select one blogspot",("dropdown to select","Uipath","RPA today","Automation Anywhere","Automation Edge","Softomotive","SAP","Forrester"))
if checkbox == "Uipath":
    x = choose_blog("https://www.uipath.com/blog/")
    path = x[89]
    st.success("Successfully scraped the recent article")
if checkbox == "RPA today":
    x = choose_blog("https://www.rpatoday.net/")
    path = x[17]
    st.success("Successfully scraped the recent article")
if checkbox == "Automation Anywhere":
    w = choose_blog("https://www.automationanywhere.com/company/blog")
    path = urljoin("https://www.automationanywhere.com",str(w[104]))
    st.success("Successfully scraped the recent article")
if checkbox == "Automation Edge":
    x = choose_blog("https://automationedge.com/blogs/")
    path = x[83]
    st.success("Successfully scraped the recent article")
if checkbox == "Softomotive":
    x = choose_blog("https://www.softomotive.com/blog-news-events/")
    path = x[49
    st.success("Successfully scraped the recent article")
if checkbox == "SAP":
    x = choose_blog("https://blogs.sap.com/tag/rpa/")
    path = x[49]
    st.success("Successfully scraped the recent article")
if checkbox == "Forrester":
    x = choose_blog("https://go.forrester.com/blogs/category/robotic-process-automation-rpa/")
    path = x[105]
    st.success("Successfully scraped the recent article")
if st.button("Get Summary & Details "):
    display2 = apicall_summary(path=path)
    st.success("Url : {}".format(display2[0]))
    st.success("summary : {}".format(display2[1]))