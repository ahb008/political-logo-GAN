import requests
import urllib
import time
from PIL import Image

from bs4 import BeautifulSoup
from selenium import webdriver

capdURL = "https://www.politicsanddesign.com/"

#Initializing the chrom driver required for selenium
#TODO: change this so the function searches machine for chromedriver
driver = webdriver.Chrome(executable_path="/Users/andrewbass/Desktop/bad_answers/Tech_Projects/chromedriver")

driver.get(capdURL)
time.sleep(3)

bottom_height = driver.execute_script("return document.body.scrollHeight")

#Loop to scroll and dynamically load the page
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load
    time.sleep(1)
    new_bottom = driver.execute_script("return document.body.scrollHeight")
    if new_bottom == bottom_height:
        break
    bottom_height = new_bottom

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

#Finds div that contains all images
imageGallery = soup.find('div', 'gallery__medium')
images = imageGallery.findAll("img")

print(len(images))

#Downloads images using src URL
for idx, image in enumerate(images):
    imageURL = "https:" + image.attrs['src'].split(" ", 1)[0]
    img = Image.open(requests.get(imageURL, stream=True).raw)
    img.save('/Users/andrewbass/Desktop/bad_answers/tech_projects/political-logo-GAN/data/' + str(idx) + '.jpg', 'JPEG')

driver.quit()