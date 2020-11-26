import requests
url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
querystring = {"sentences":"5",
               "url":"https://www.uipath.com/blog/improving-data-privacy-using-process-mining"}

headers = {
    'accept': "application/json",
    'x-rapidapi-key': "82f634005emsha418ca5ea3be960p110c9bjsn150bfa1b8522",
    'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)