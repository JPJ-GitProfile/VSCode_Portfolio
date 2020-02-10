from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"

# opening the connection and grabbing the page
cClient = uReq(my_url)
page_html = cClient.read()
cClient.close()

# html parsing
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"item-container"})

# get first container
container = containers[0]

# get the "a" tag that has the title so we can get the name of the
# graphics card
item_title = container.findAll("a", {"class":"item-title"})

# store the title
graphicCardName = item_title[0].string

# test


