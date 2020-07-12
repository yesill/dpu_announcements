import requests
from bs4 import BeautifulSoup as BS

class announcement():
    
    def __init__(self,title,text,date):
        self.title = title
        self.text = text
        self.date = date
        
    def show(self):
        print("\t{}\t{}\n".format(self.title,self.date))
        print("{}".format(self.text))
		
announcement_links = list()
announcements = list()

url_base = "http://bilgisayar.dpu.edu.tr/"

soup = BS(requests.get(url_base).content,"html.parser")

for i in soup.find_all('a'):
    try:
        if "duyuru" in str(i): #str ye cevirmemiz gerek degilse obje olarak bakiyor
            announcement_links.append(url_base+i.get('href'))
    except:
        continue
		
for a in announcement_links:
    title = str()
    text = str()
    date = str()
    soup_a = BS(requests.get(a).content,"html.parser")
    #title
    for i in soup_a.find_all("div", class_="col-md-9 sayfa kenarlik-sag"):
        for j in i.find_all("h1"):
            title = j.text
    #text
    for i in soup_a.find_all("div", class_="sayfa-icerik"):
            text += i.text
    #date
    for i in soup_a.find_all("div", class_="col-md-6"):
        for j in i.find_all("small"):
            date += j.text.split("/",1)[0]
    #creating announcement object
    announcements.append(announcement(title,text,date))
	
announcements[0].show()
announcements[1].show()
announcements[2].show()