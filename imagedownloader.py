from BeautifulSoup import BeautifulSoup
import requests
import urllib2
import re
#importing requirements

html_page = urllib2.urlopen("https://unsplash.com/")
#opening the webpage

soup = BeautifulSoup(html_page)
#instance of the BeautifulSoup class

images = []
#declaring the list

for img in soup.findAll('img'):
    images.append(img.get('src'))
#getting the image source tags from the webpage

image_url = images[1]
#We found out that the image we want to download is at the index : 1

img_data = requests.get(image_url).content
with open('downloaded_image.jpg', 'wb') as handler:
    handler.write(img_data)
#downloading the image using requests

