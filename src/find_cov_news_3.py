import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import http
import time
#from lxml import etree
import re

def crawl():

    url = "https://coronavirus.bg/bg/news/"  #158
    nodes = list()
    covnews = open("all_covreportnews(3).txt",encoding="utf-8", mode="r")
    dat = open("all_raw_numbers(4).txt",encoding="utf-8", mode="w")
    
    for line in covnews:
        nodes.append(line.split()[0])
    #TODO: check for errors
    for node in nodes:
        ur = url+str(node)
        req = Request(ur, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        mal = re.findall('мъж на ([0-9]+)',webpage.decode())
        fem = re.findall('жена на ([0-9]+)',webpage.decode())
        print
        for el in mal:
            dat.write(el)
            dat.write(",")
        for el in fem:
            dat.write(el)
            dat.write(",")
        time.sleep(0.1)
        print (node)
    dat.write("0") #TODO - to make it delete the last ','
    dat.close()
    covnews.close()
    
if __name__ == '__main__':
    crawl()
