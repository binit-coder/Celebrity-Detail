import requests
from bs4 import BeautifulSoup

celeb = input("Enter Celebrity Name :  ").split()
celeb_name =  celeb[0]+"_"+celeb[1] 

url = "https://en.wikipedia.org/wiki/"
celeb_url = url + celeb_name

r = requests.get(celeb_url)  #fetching requests from given URL
data = r.text 
soup = BeautifulSoup(data,"html.parser")

for i in soup.findAll("table",{"class":"infobox"}):
    for j in i.find_all("tr"):
        print(j.text)




