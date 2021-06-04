import requests
import urllib
import time
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver

capdURL = "https://www.politicsanddesign.com/"

#Initializing the chrom driver required for selenium
#TODO: change this so the function searches machine for chromedriver
driver = webdriver.Chrome(executable_path="/Users/andrewbass/Desktop/bad_answers/Tech_Projects/chromedriver")


driver.get(capdURL)
time.sleep(1)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

#Finds div that contains all images
imageGallery = soup.find('div', 'gallery__medium')
images = imageGallery.findAll("img")

#Downloads images using src
for idx, image in enumerate(images):
    imageURL = "https:" + image.attrs['src'].split(" ", 1)[0]
    urllib.request.urlretrieve(imageURL, idx)

driver.quit()

print("AAAAAAAAAAAAA")