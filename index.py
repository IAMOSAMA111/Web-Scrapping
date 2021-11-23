from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime






app = Flask(__name__)

_headings = []
_article_links = []
_intro=[]
_modifieddata=[]
_headings1 = []
_article_links1 = []
_intro1=[]
_imagelink1=[]
_modifieddata1=[]


def firstPage():
    url = "https://www.urdupoint.com/en/news/agriculture.html"
    r = requests.get(url)
     
    htmlContent = r.content
    _soup = BeautifulSoup(htmlContent,'html.parser')

    data = (_soup.find_all('div',class_='txt_box'))
    length = len(data)
   
    with open("data.html","w", encoding='utf-8') as f:
        for i in range(length):
            
            f.write(str(data[i]))
            with open("check.html","w+", encoding='utf-8') as c:
                c.write(str(data[i]))
                
            c.close()
            with open("check.html","r") as d:
                cont = d.read()
            d.close()

            _soupC = BeautifulSoup(cont,'html.parser')
            _check=[]
            for link in _soupC.find_all('a'):
                
                _check.append(link.get('href'))
               
            
            if(len(_check)==2):
                _article_links.append(_check[1])
                
            else:
                _article_links.append(_check[0])
            
    f.close()

    with open("data.html","r")as html_file:
        content = html_file.read()
        _soup = BeautifulSoup(content,'html.parser')
        # for link in _soup.find_all('a'):
        #     _article_links.append(link.get('href'))      
        _datalength = (len(_article_links))

        for heading in _soup.find_all('h4'):
            _headings.append(heading.get_text())
        
        for intro in _soup.find_all('p'):
            _intro.append(intro.get_text()) 
        

def secondPage():
    url = "https://www.urdupoint.com/en/news/agriculture-updates2.html"
    r = requests.get(url)
     
    htmlContent = r.content
    _soup = BeautifulSoup(htmlContent,'html.parser')

    data = (_soup.find_all('div',class_='txt_box'))
    length = len(data)
   
    with open("data1.html","w") as f:
        for i in range(length):
            
            f.write(str(data[i]))
            with open("check.html","w+") as c:
                c.write(str(data[i]))
                
            c.close()
            with open("check.html","r") as d:
                cont = d.read()
            d.close()

            _soupC = BeautifulSoup(cont,'html.parser')
            _check=[]
            for link in _soupC.find_all('a'):
                
                _check.append(link.get('href'))
               
            
            if(len(_check)==2):
                _article_links.append(_check[1])
                
            else:
                _article_links.append(_check[0])
            
    f.close()

    with open("data1.html","r")as html_file:
        content = html_file.read()
        _soup = BeautifulSoup(content,'html.parser')
        # for link in _soup.find_all('a'):
        #     _article_links.append(link.get('href'))      
        _datalength = (len(_article_links))

        for heading in _soup.find_all('h4'):
            _headings.append(heading.get_text())
        
        for intro in _soup.find_all('p'):
            _intro.append(intro.get_text())       

def jsonCompilation():
    length = len(_headings)
    for i in range (length):
        _dict_data = {
            "heading": _headings[i],
            "intro": _intro[i],
            "link":_article_links[i]
        }
        _modifieddata.append(_dict_data)
    
    _final_dictionary ={"data":_modifieddata}
    json_object = json.dumps(_final_dictionary, indent = 4)  

    

    with open("data.json","w+")as f:
        f.write(json_object)

    print('JSON IS MADE')
    return json_object

def firstPageInternational():
    url = "https://www.growingproduce.com/fruits/"
    r = requests.get(url)

    htmlContent = r.content
    _soup = BeautifulSoup(htmlContent,'html.parser')

    data = (_soup.find_all('article',class_='inline-post-section section-full'))
    length = len(data)

    with open("data3.html", "w+") as f:
        for i in range (length):
            f.write(str(data[i]))
            with open("growingFruitArticleLink.html","w") as c:
                c.write(str(data[i]))
            c.close()
            with open("growingFruitArticleLink.html","r") as d:
                linkraw = d.read()
            d.close()

            _soupL = BeautifulSoup(linkraw,'html.parser')

            refinelink =_soupL.find_all("div",class_="col-xs-5 col-md-4 post-image-col hidden-xs")

            
            with open("growingFruitArticleLink.html","w") as c:
                c.write(str(refinelink))
            c.close()
            with open("growingFruitArticleLink.html","r") as d:
                linkraw = d.read()
            d.close()
            _soupL = BeautifulSoup(linkraw,'html.parser')
            for link in _soupL.find_all('a'):
                _article_links1.append(link.get('href'))
            for link in _soupL.find_all('img'):
                _imagelink1.append(link.get('data-src'))
            
    f.close()

    with open("data3.html","r")as html_file:
        content = html_file.read()
        _soup = BeautifulSoup(content,'html.parser')
        for intro in _soup.find_all('div',class_='post-excerpt hidden-xs'):
            _intro1.append(intro.get_text())
        for heading in _soup.find_all('h3',class_='post-title'):
            _headings1.append(heading.get_text())
    html_file.close()

def secondPageInternational():
    url = "https://www.growingproduce.com/fruits/page/2/"
    r = requests.get(url)

    htmlContent = r.content
    _soup = BeautifulSoup(htmlContent,'html.parser')

    data = (_soup.find_all('article',class_='inline-post-section section-full'))
    length = len(data)

    with open("data3.html", "w+") as f:
        for i in range (length):
            f.write(str(data[i]))
            with open("growingFruitArticleLink.html","w") as c:
                c.write(str(data[i]))
            c.close()
            with open("growingFruitArticleLink.html","r") as d:
                linkraw = d.read()
            d.close()

            _soupL = BeautifulSoup(linkraw,'html.parser')

            refinelink =_soupL.find_all("div",class_="col-xs-5 col-md-4 post-image-col hidden-xs")

            
            with open("growingFruitArticleLink.html","w") as c:
                c.write(str(refinelink))
            c.close()
            with open("growingFruitArticleLink.html","r") as d:
                linkraw = d.read()
            d.close()
            _soupL = BeautifulSoup(linkraw,'html.parser')
            for link in _soupL.find_all('a'):
                _article_links1.append(link.get('href'))
            for link in _soupL.find_all('img'):
                _imagelink1.append(link.get('data-src'))
            
    f.close()

    with open("data3.html","r")as html_file:
        content = html_file.read()
        _soup = BeautifulSoup(content,'html.parser')
        for intro in _soup.find_all('div',class_='post-excerpt hidden-xs'):
            _intro1.append(intro.get_text())
        for heading in _soup.find_all('h3',class_='post-title'):
            _headings1.append(heading.get_text())
    html_file.close()
    
    

def jsonCompilationInternational():
    length = len(_headings1)
    for i in range (length):
        _dict_data1 = {
            "heading": _headings1[i],
            "intro": _intro1[i],
            "img":_imagelink1[i],
            "link":_article_links1[i]
        }
        _modifieddata1.append(_dict_data1)
    _final_dictionary ={"data":_modifieddata1}
    json_object = json.dumps(_final_dictionary, indent = 5)  
    with open("data1.json","w+")as f:
        f.write(json_object)
    
    return (json_object)


firstPageInternational()
secondPageInternational() 
jsonCompilationInternational()
firstPage()
secondPage()
jsonCompilation()
    

