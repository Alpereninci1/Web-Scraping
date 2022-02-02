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

def textWrite(txt):
    with open("output3.txt", "w") as txt_file:
        for line in txt:
           txt_file.write(line + "\n")



driver_path="C:\\Users\\Monster\\Desktop\\Selenium\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

#print(type(driver))
driver.get("https://kararlar.sayistay.gov.tr/dk/")
myPageTitle=driver.title
print(myPageTitle)

driver.find_element_by_name("BUL").click()#tüm sayfaları getiren komut


table = driver.find_element_by_class_name("conlist")
trs = table.find_elements_by_tag_name("tr")

links = []

page_count=driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td[2]/form/button[2]").get_attribute("value")

page_counts=int(page_count)+1

for i in range(1,page_counts):
    
    req = requests.post("https://kararlar.sayistay.gov.tr/dk/", {
        "pg": i,
        "TARIH1": 2006,
        "TARIH2": 2022,
        "BUL": "KARARBUL"
    })
    for i in  range(1,len(trs)):
        tr = trs[i]

    link = tr.find_element_by_tag_name("a").get_attribute("href")
    links.append(link)
    textWrite(links)
    

   





