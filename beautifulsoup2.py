from bs4 import BeautifulSoup
import requests

def textWrite2(txt,i):
    for j in range(1,i):
        with open('%d_doc.txt' %j,'a', encoding='utf-8') as f:
           f.write(txt)

def textWrite(txt,i):
    with open('%d_doc.txt' %i,'a', encoding='utf-8') as f:
        f.write(txt)
   


lines = []
with open('log.txt', 'r') as f:
    lines = f.readlines()


for link in lines:
    l=len(lines)
    link = "https://kararlar.sayistay.gov.tr/dk/" + link.replace('\n', '')
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    
    text = soup.find("p").text
    textWrite(text,l)




