# Use the Request library
import requests
# Set the target webpage
url = 'http://172.18.58.238/snow/'
r = requests.get(url)
# This will get the full page
print(r.text)
#This will get the status code
print("Status code, OK:")
print("\t*",r.status_code)
#This will just get the headers
h = requests.head(url)
print("Header:")
print("*********")
#To print line by line
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("*********")
import webbrowser
url = 'http://172.18.58.238/snow'
webbrowser.open(url)
#This will modify the headers user-agent
headers = {
    'User-Agent': 'Mobile'
}
#Test it on external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2,headers=headers)
print(rh.text)

import scrapy
class NewSpider(scrapy.Spider):
    name = "Project"
    start_urls = ["http://172.18.58.238/"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
