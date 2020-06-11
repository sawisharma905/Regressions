# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:04:40 2020

@author: Dell
"""
import bs4
import requests
import csv

# with open("simple.html") as html_file:
#     soup=bs4.BeautifulSoup(html_file,'lxml')
    
# #print(soup.prettify())

# match=soup.a.text
# print(match)

# #to get a particular part access
# match1=soup.find('div',class_="article")
# #print(match1)
# #we have put a _ after class as class is a keyword in pyt so to keep it different from that, we used _

# #scrapping the headline and summary from the web page
# headline=match1.h2.a.text
# print(headline)

# summary=match1.p.text
# print(summary)

# #find_all will help to find list of all the matching tags that match that arguement
# for article in soup.find_all('div',class_='article'):
#     headline=article.h2.a.text
#     print(headline)

#     summary=article.p.text
#     print(summary)
    
#     print()

source=requests.get('https://coreyms.com/').text
#requests.get('https://coreyms.com/')this returns a response object
#.text is added to get the source code from that object
soup=bs4.BeautifulSoup(source,'lxml')
#print(soup.prettify())

csv_file=open('scrap_practice.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in soup.find_all('article'):

    headline=article.h2.a.text
    print(headline)
    print()
    summary=article.find('div',class_='entry-content').p.text
    print(summary)
    print()
    #to get the video link
    
    # vid_src=article.find('iframe', class_='youtube-player')['src']
    # #other way to do the same:vid_src= article.iframe['src']
    # #print(vid_src)
    
    # #to get the id of the video spliting the link obtained at / 
    # vid_id=vid_src.split('/')[4]
    # vid_id=vid_id.split('?')[0]
    
    # yt_link="https://youtube.com/watch?v={}".format(vid_id)
    # print(yt_link)

    # print()
    
#it is possible to happen that during scrapping some of our data we may not have
#some items available, this may break our search cycle
#for eg some link or image missing
#so we need to overcome this.
#we should put them in try/except block
    
    try:
        vid_src= article.iframe['src']
        #other way to do the same:vid_src= article.iframe['src']
        #print(vid_src)
        
        #to get the id of the video spliting the link obtained at / 
        vid_id=vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]
        
        yt_link="https://youtube.com/watch?v={}".format(vid_id)
        
    except Exception as e:
        yt_link=None
        
    print(yt_link)    
    print()
    csv_writer.writerow([headline,summary,yt_link])    
    
csv_file.close()