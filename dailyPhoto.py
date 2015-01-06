#!/usr/bin/python

import requests
import bs4
import csv

captions = []
links = []

def main():
    nextLink = 'http://binghamton.edu/photos/'
    currentDay = requests.get(nextLink)
    soup = bs4.BeautifulSoup(currentDay.text)
    #caption = soup.select(".caption")[1].p
    #caption = soup.find('p').contents[0]
    #print (caption) # debug
    csvfile = open('captions.csv', 'wb')
    writer = csv.writer(csvfile)

    while nextLink not in links:
        captions.append(caption)
        links.append(nextLink)
        nextLink = soup.select('a[href^="http://www.binghamton.edu/photos/index.php/gallery/archives/"]')[0].attrs.get('href')
        print (nextLink) # debug
        currentDay = requests.get(nextLink)
        soup = bs4.BeautifulSoup(currentDay.text)
        #caption = soup.select(".caption")[1].p
        caption = soup.find('p').contents[0]
        print (caption) # debug
        writer.writerow( (caption.encode('utf-8'), nextLink) )

main()
