#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 14:56:10 2015

@author: rflamary
"""

import bs4
import urllib
#import html2text
import argparse


def clean_name(txt):
    #return html2text.html2text(txt)
    res=txt.replace('\n','')
    res=res.replace('\r','')
    while res[0]==' ':
        res=res[1:]
    while res[-1]==' ':
        res=res[:-1]        
    return res




                
#%% 
                
parser = argparse.ArgumentParser(description='Get Kaggle ranking')   

parser.add_argument('url',help='url of the competition of the form https://www.kaggle.com/c/{competition}/leaderboard')
parser.add_argument('list', metavar='filter', type=str, nargs='*', help='list of strings that have to be in the participant name for filtering')

args = parser.parse_args()  


response = urllib.FancyURLopener().open(args.url)

data = response.read()      # a `bytes` object
text = data#.decode('utf-8') # a `str`; this step can't be used if data is binary

soup = bs4.BeautifulSoup(text)


lstr=soup.find_all('tr')
lst=list()
for i in range(1,len(lstr)):
    try:  
        if lstr[i]['id']:
            ltd=lstr[i].find_all('td')
            dic=dict()
            dic['name']=clean_name(lstr[i].a.text)
            dic['rank']=ltd[0].text
            dic['perf']=clean_name(ltd[3].text)
            dic['nbsub']=clean_name(ltd[4].text)
            dic['last']=clean_name(ltd[5].text)
            lst.append(dic)
        
    except KeyError:
        pass    

filt=args.list
         
print 'Rank\tPerformance\tName'
if filt:
    for item in lst:
        pr=0
        for f in filt:
            if f in item['name'] and pr==0:
                print item['rank'],'\t',item['perf'],'\t',item['name']
                pr=1
else:
    for item in lst:
        print item['rank'],'\t',item['perf'],'\t',item['name']         

