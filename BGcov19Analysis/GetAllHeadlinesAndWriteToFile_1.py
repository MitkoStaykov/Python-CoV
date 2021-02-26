import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup

#    The information we need - the address, the date, 
#    the headline to check if it is relevant

def scrape():

    allcov = open("all_headlines(1).txt",encoding="utf-8", mode="w")
    
    url = "https://coronavirus.bg/bg/news"
    
    number_of_pages = 10 #can be automated 105 default
    
    for i in range (1,number_of_pages):
        ur = url+"?p="+str(i)
        print (ur)
        req = Request(ur, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()#.decode()
        soup = BeautifulSoup(webpage, 'html.parser')
        
        news = soup.select('.listing-news-title')
        dates = soup.select('.listing-news-date')
        for new in news:
            par = new.parent
            date = par.findNext('p')
            node = par.findNext('a')
            allcov.write(node['href'])
            allcov.write("\n")
            allcov.write(date.get_text())
            allcov.write("\n")
            allcov.write(new.get_text())
            allcov.write("\n")
        time.sleep(1)
        
    allcov.close()
        
if __name__ == '__main__':
    scrape()