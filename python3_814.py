# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:09:16 2020

@author: rong2
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input ('Enter count: '))
position = int(input ('Enter position: '))

for i in range (count):
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup (html,'html.parser')
    tags = soup ('a')
    link = tags[position-1].get('href',None)
    url = link 
print (url)

  
    
    
    