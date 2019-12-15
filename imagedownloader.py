from BeautifulSoup import BeautifulSoup
import requests
import urllib2
import re

html_page = urllib2.urlopen("https://unsplash.com/")
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

image_url = images[1]

img_data = requests.get(image_url).content
with open('downloaded_image.jpg', 'wb') as handler:
    handler.write(img_data)



