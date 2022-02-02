from lib2to3.pgen2.driver import Driver
from msilib.schema import File
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import time
import string


driver_path="C:\\Users\\Monster\\Desktop\\Selenium\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

def textWrite2(txt,i):
    for j in range(1,i):
        with open('%d_doc.txt' %j,'a', encoding='utf-8') as f:
           f.write(txt)

def textWrite(txt):
    with open('doc.txt' ,'a', encoding='utf-8') as f:
        f.write(txt)
   


lines = []
with open('log.txt', 'r') as f:
    lines = f.readlines()


for link in lines:
    link = "https://kararlar.sayistay.gov.tr/dk/" + link.replace('\n', '')
    driver.get(link)
    text=driver.find_element_by_tag_name("p").text
    textWrite(text)