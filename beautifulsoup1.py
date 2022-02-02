import requests
from bs4 import BeautifulSoup
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


def log(link):
    with open('log2.txt', 'a', encoding='utf-8') as f:
        f.write(link + '\n')

driver_path="C:\\Users\\Monster\\Desktop\\Selenium\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

driver.get("https://kararlar.sayistay.gov.tr/dk/")

driver.find_element_by_name("BUL").click()

page_count=driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td[2]/form/button[2]").get_attribute("value")

page_counts=int(page_count)+1

for i in range(1,page_counts):
    
    req = requests.post("https://kararlar.sayistay.gov.tr/dk/", {
        "pg": i,
        "TARIH1": 2006,
        "TARIH2": 2022,
        "BUL": "KARARBUL"
    })

    soup = BeautifulSoup(req.text, "html.parser")
    
    table = soup.find("table", {"class": "conlist"})
    list_a = table.find_all("a")

    for a in list_a:
        link = a.get("href")
        log(link)

